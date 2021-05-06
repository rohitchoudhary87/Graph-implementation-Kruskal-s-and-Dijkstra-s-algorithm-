# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:56:11 2021

@author: rohit
"""

#Dijkstra's algorithm
inf = float("inf")
start = "3"
stop = "19"

graph = {}

graph["0"] = {}
graph["0"]["1"] = 15
graph["0"]["4"] = 8
graph["0"]["15"] = 14
graph["0"]["18"] = 4
graph["0"]["19"] = 15

graph["1"] = {}
graph["1"]["2"] = 17
graph["1"]["4"] = 9
graph["1"]["13"] = 19
graph["1"]["15"] = 14
graph["1"]["19"] = 16

graph["2"] = {}
graph["2"]["3"] = 20
graph["2"]["6"] = 14
graph["2"]["16"] = 1

graph["3"] = {}
graph["3"]["6"] = 12
graph["3"]["8"] = 13
graph["3"]["11"] = 1
graph["3"]["16"] = 2

graph["4"] = {}
graph["4"]["12"] = 14
graph["4"]["15"] = 7
graph["4"]["18"] = 20
graph["4"]["19"] = 1

graph["5"] = {}
graph["5"]["8"] = 9
graph["5"]["14"] = 8
graph["5"]["15"] = 16
graph["5"]["17"] = 16
graph["5"]["19"] = 4

graph["6"] = {}
graph["6"]["11"] = 13
graph["6"]["16"] = 15
graph["6"]["17"] = 16

graph["7"] = {}
graph["7"]["8"] = 6
graph["7"]["14"] = 14
graph["7"]["16"] = 14
graph["7"]["17"] = 4

graph["8"] = {}
graph["8"]["14"] = 20
graph["8"]["15"] = 7
graph["8"]["17"] = 12
graph["8"]["19"] = 5

graph["9"] = {}
graph["9"]["10"] = 16
graph["9"]["12"] = 6
graph["9"]["13"] = 11
graph["9"]["18"] = 14

graph["10"] = {}
graph["10"]["12"] = 20
graph["10"]["13"] = 11
graph["10"]["18"] = 3

graph["11"] = {}
graph["11"]["14"] = 17
graph["11"]["16"] = 6

graph["12"] = {}
graph["12"]["13"] = 7

graph["13"] = {}
graph["13"]["18"] = 8

graph["14"] = {}
graph["14"]["17"] = 6

graph["15"] = {}
graph["15"]["19"] = 2

graph["16"] = {}
graph["17"] = {}
graph["18"] = {}
graph["19"] = {}

costs = {}
parents = {}
for node in graph:
    costs[node] = inf
    parents[node] = {}
    
costs[start] = 0

def find_cheapest_node(costs, not_checked):
    cheapest_node = None
    lowest_cost = inf
    for node in not_checked:
        if costs[node] <= lowest_cost:
            lowest_cost = costs[node]
            cheapest_node = node
    return cheapest_node

if __name__ == "__main__":
    not_checked = [node for node in costs]
    node = find_cheapest_node(costs, not_checked)
    while not_checked:
        print(f"not checked: {not_checked}")
        cost = costs[node]
        child_cost = graph[node]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                parents[c] = node
        
        not_checked.pop(not_checked.index(node))
        node = find_cheapest_node(costs, not_checked)
        
    print(f"costs: {costs}")
    print(f"the cost to go from {start} to {stop} is {costs[stop]}")
    
    #printing the path
    if costs[stop] < inf:
        path = [stop]
        i = 0
        while start not in path:
            path.append(parents[path[i]])
            i += 1
            
        print(f"The shortest path is {path[::-1]}")
    else:
        print("No path found")


# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:01:19 2021

@author: rohit
"""
"""
#Kruskal's Algorithm
class Graph:
    #initializing the total number of vertices(20 in our case), and an array to store the graph
	def __init__(self, totalNodes):
		self.V = totalNodes
		self.graph = [] 

	# Adding an edge
	def addAnEdge(self, u, v, weight):
		self.graph.append([u, v, weight])
        
    #finding the set of the element at i
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])
    
    
    #In kruskal's algorithm, we need to find the union of two sets a and b
	# We will attach a tree with a smaller rank under the one with higher rank
	# Also, if rank are same then we can go ahead with any one by incrementing its rank by 1
	def union(self, parentNode, ranking, a, b):
		aRoot = self.find(parentNode, a)
		bRoot = self.find(parentNode, b)

		if ranking[aRoot] < ranking[bRoot]:
			parentNode[aRoot] = bRoot
		elif ranking[aRoot] > ranking[bRoot]:
			parentNode[bRoot] = aRoot

		else:
			parentNode[bRoot] = aRoot
			ranking[aRoot] += 1

	# main Kruskal's function
    # we first sort edges in ascending order of weights 
    # we select the smallest edge first.
    # and for every next iteration if including the edge result in a cycle, we discard that edge.
	def KruskalsMST(self):
		res = []
		i = 0
		j = 0

		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parentArr = []
		rank = []

		for node in range(self.V):
			parentArr.append(node)
			rank.append(0)

		while j < self.V - 1:
			u, v, weight = self.graph[i]
			i = i + 1
			x = self.find(parentArr, u)
			y = self.find(parentArr, v)

			if x != y:
				j = j + 1
				res.append([u, v, weight])
				self.union(parentArr, rank, x, y)

		minCost = 0
		print ("The flow of the MST is as follows-")
		for u, v, weight in res:
			minCost += weight
			print("%d - %d cost = %d" % (u, v, weight))
		print("The cost of the MST is" , minCost)

# Driver code
graph = Graph(20)

graph.addAnEdge(0, 1, 15)
graph.addAnEdge(0, 4, 8)
graph.addAnEdge(0, 15, 14)
graph.addAnEdge(0, 18, 4)
graph.addAnEdge(0, 19, 15)
graph.addAnEdge(1, 2, 17)
graph.addAnEdge(1, 4, 9)
graph.addAnEdge(1, 13, 19)
graph.addAnEdge(1, 15, 14)
graph.addAnEdge(1, 19, 16)
graph.addAnEdge(2, 3, 20)
graph.addAnEdge(2, 6, 14)
graph.addAnEdge(2, 16, 1)
graph.addAnEdge(3, 6, 12)
graph.addAnEdge(3, 8, 13)
graph.addAnEdge(3, 11, 1)
graph.addAnEdge(3, 16, 2)
graph.addAnEdge(4, 12, 14)
graph.addAnEdge(4, 15, 7)
graph.addAnEdge(4, 18, 20)
graph.addAnEdge(4, 19, 1)
graph.addAnEdge(5, 8, 9)
graph.addAnEdge(5, 14, 8)
graph.addAnEdge(5, 15, 16)
graph.addAnEdge(5, 17, 16)
graph.addAnEdge(5, 19, 4)
graph.addAnEdge(6, 11, 13)
graph.addAnEdge(6, 16, 15)
graph.addAnEdge(6, 17, 16)
graph.addAnEdge(7, 8, 6)
graph.addAnEdge(7, 14, 14)
graph.addAnEdge(7, 16, 14)
graph.addAnEdge(7, 17, 4)
graph.addAnEdge(8, 14, 20)
graph.addAnEdge(8, 15, 7)
graph.addAnEdge(8, 17, 12)
graph.addAnEdge(8, 19, 5)
graph.addAnEdge(9, 10, 16)
graph.addAnEdge(9, 12, 6)
graph.addAnEdge(9, 13, 11)
graph.addAnEdge(9, 18, 14)
graph.addAnEdge(10, 12, 20)
graph.addAnEdge(10, 13, 11)
graph.addAnEdge(10, 18, 3)
graph.addAnEdge(11, 14, 17)
graph.addAnEdge(11, 16, 6)
graph.addAnEdge(12, 13, 7)
graph.addAnEdge(13, 18, 8)
graph.addAnEdge(14, 17, 6)
graph.addAnEdge(15, 19, 2)


# invoking the Kruskal's function
graph.KruskalsMST()

"""


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:43:42 2021

@author: rohit
"""

"""
# Graph implementation with adjacency list
# Addind an edge
def addAnEdge(adjacent, u, v, weight):
     
    adjacent[u].append([v, weight])
    adjacent[v].append([u, weight])
    return adjacent
 
# Printing the adjacency list
def printTheGraph(adjacent, V):
     
    v, w = 0, 0
    for u in range(V):
        print("Node", u, "is connected with the Nodes ->")
 
        for each in adjacent[u]:
            v = each[0]
            w = each[1]
            print("\t", v, "edge weight =", w)
             
        print()
 
# Driver code
if __name__ == '__main__':
     
    V = 20
    adjacent = [[] for i in range(V)]
    
    adjacent = addAnEdge(adjacent, 0, 1, 15)
    adjacent = addAnEdge(adjacent, 0, 4, 8)
    adjacent = addAnEdge(adjacent, 0, 15, 14)
    adjacent = addAnEdge(adjacent, 0, 18, 4)
    adjacent = addAnEdge(adjacent, 0, 19, 15)
    adjacent = addAnEdge(adjacent, 1, 2, 17)
    adjacent = addAnEdge(adjacent, 1, 4, 9)
    adjacent = addAnEdge(adjacent, 1, 13, 19)
    adjacent = addAnEdge(adjacent, 1, 15, 14)
    adjacent = addAnEdge(adjacent, 1, 19, 16)  
    adjacent = addAnEdge(adjacent, 2, 3, 20)
    adjacent = addAnEdge(adjacent, 2, 6, 14)
    adjacent = addAnEdge(adjacent, 2, 16, 1) 
    adjacent = addAnEdge(adjacent, 3, 6, 12)
    adjacent = addAnEdge(adjacent, 3, 8, 13)
    adjacent = addAnEdge(adjacent, 3, 11, 1)
    adjacent = addAnEdge(adjacent, 3, 16, 2)
    adjacent = addAnEdge(adjacent, 4, 12, 14)
    adjacent = addAnEdge(adjacent, 4, 15, 7)
    adjacent = addAnEdge(adjacent, 4, 18, 20)
    adjacent = addAnEdge(adjacent, 4, 19, 1)
    adjacent = addAnEdge(adjacent, 5, 8, 9)
    adjacent = addAnEdge(adjacent, 5, 14, 8)
    adjacent = addAnEdge(adjacent, 5, 15, 16)
    adjacent = addAnEdge(adjacent, 5, 17, 16)
    adjacent = addAnEdge(adjacent, 5, 19, 4) 
    adjacent = addAnEdge(adjacent, 6, 11, 13)
    adjacent = addAnEdge(adjacent, 6, 16, 15)
    adjacent = addAnEdge(adjacent, 6, 17, 16)
    adjacent = addAnEdge(adjacent, 7, 8, 6)
    adjacent = addAnEdge(adjacent, 7, 14, 14)
    adjacent = addAnEdge(adjacent, 7, 16, 14)
    adjacent = addAnEdge(adjacent, 7, 17, 4) 
    adjacent = addAnEdge(adjacent, 8, 14, 20)
    adjacent = addAnEdge(adjacent, 8, 15, 7)
    adjacent = addAnEdge(adjacent, 8, 17, 12)
    adjacent = addAnEdge(adjacent, 8, 19, 5)
    adjacent = addAnEdge(adjacent, 9, 10, 16)
    adjacent = addAnEdge(adjacent, 9, 12, 6)
    adjacent = addAnEdge(adjacent, 9, 13, 11)
    adjacent = addAnEdge(adjacent, 9, 18, 14) 
    adjacent = addAnEdge(adjacent, 10, 12, 20)
    adjacent = addAnEdge(adjacent, 10, 13, 11)
    adjacent = addAnEdge(adjacent, 10, 18, 3)
    adjacent = addAnEdge(adjacent, 11, 14, 17)
    adjacent = addAnEdge(adjacent, 11, 16, 6)
    adjacent = addAnEdge(adjacent, 12, 13, 7)
    adjacent = addAnEdge(adjacent, 13, 18, 8) 
    adjacent = addAnEdge(adjacent, 14, 17, 6)
    adjacent = addAnEdge(adjacent, 15, 19, 2)
    
 
    printTheGraph(adjacent, V)
    
    """