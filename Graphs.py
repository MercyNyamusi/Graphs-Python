import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random


def ER(n, p):
    result = ""
    """
    function to generate a random graph
    :param n: order of the graph
    :param p: probability that ywo edges are connected
    :return: graph object
    """
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)
    vertex_dict = degree(E)
    x = connected(vertex_dict[1], n)
    if x == 1:
        print("Graph is not connected\n")
        return result, g
    else:
        counter = 0
        print("Graph is connected")
        for i in vertex_dict[0]:
            if i % 2 != 0:  # determines whether graph is euler circuit by checking if all nodes have an even degree
                counter += 1
    if counter > 0:
        result = 'No'
        print("No")
        print("Graph does not have an Euler circuit\n")
    else:
        result = 'Yes'
        print("Yes")
        print("Graph has an Euler circuit\n")
    return result, g


def degree(E):
    """
    function to determine the degree of each node
    :param E: set containing the edges of a graph
    :return: vertices_list - a list of the degree of each node on the graph
    :return: vertex_dict - a dictionary mapping every node to its neighbours
    """
    vertices_list = []
    vertex_dict = {}
    for i in range(n):
        count = 0
        vertex_list = []
        for item in E:
            if i in item:
                if item[1] != i:
                    vertex_list.append(item[1])
                else:
                    vertex_list.append(item[0])
                count += 1
        vertex_list.sort()
        vertex_dict[i] = vertex_list
        vertices_list.append(count)
    return vertices_list, vertex_dict


def connected(sdict, n):
    """
    Function to check whether graph is connected or not
    :param sdict: dictionary mapping every node to its neighbours
    :return: 0 if graph is connected, 1 if graph is not connected
    """
    visited_node = []
    r_list = visited(0, visited_node, sdict)
    if len(set(r_list)) == n:  # checks to determine whether all nodes of the graph were visited
        return 0
    else:
        return 1


def visited(node, visited_node_list, mydict):
    """
    Function to traverse through nodes of the graph using dfs
    :param node: the node being visited
    :param visited_node_list: list of nodes that have been visited
    :param mydict: dictionary mapping every node to its neighbours
    :return: list of visited nodes
    """
    for i in mydict[node]:
        if i not in visited_node_list:
            visited_node_list.append(i)
            visited(i, visited_node_list,
                    mydict)  # calls itself recursively until all neighbours of the node have been visited
    return visited_node_list

def probability(count):
    prob = (count/10000) * 100
    print("The probability of getting a Euler circuit given that the graph is connected is {0:.7}%".format(prob))

n = 10
p = 0.4
# G = ER(n, p)
# pos = nx.spring_layout(G[1])
# nx.draw_networkx(G[1], pos)
# plt.title("Random Graph Generation Example")
# plt.show()


result_list = []
for i in range(10000):
    G = ER(n, p)
    result_list.append(G[0])
count = 0
for i in result_list:
    if i == "Yes":
        count += 1 # number of Euler circuits generated
print("Number of graphs with an Euler circuit", count)
probability(count)
