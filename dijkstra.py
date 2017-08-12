#!/usr/bin/env python
from sys import argv

def parse(inputText):
    with open(inputText, "r") as f:
        graph = {}
        for row in f.read().split('\n'):
            if row:
                row = row.split('\t')[:-1]
                graph[row[0]] = {}
                for adjacent in row[1:]:
                    nodeLength = adjacent.split(',')
                    graph[row[0]][nodeLength[0]] = int(nodeLength[1])
        return graph

def dijkstra(graph, inputNode):
    visited = {}
    unvisited = {node: None for node in graph.keys()}
    cur = inputNode
    curDist = 0
    unvisited[cur] = curDist
    while True:
        for adj, dist in graph[cur].items():
            if adj not in unvisited:
                continue
            newDist = curDist + dist
            if unvisited[adj] is None or unvisited[adj] > newDist:
                unvisited[adj] = newDist
        visited[cur] = curDist
        del unvisited[cur]
        if not unvisited:
            break
        possible = [node for node in unvisited.items() if node[1]]
        cur, curDist = sorted(possible, key = lambda x: x[1])[0]
    return visited

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage ./dijkstra.py graph.txt")
        exit()
    graph = parse(argv[1])
    lengths = dijkstra(graph, '1')
    print(lengths)
    print(lengths['7'])
    print(lengths['37'])
    print(lengths['59'])
    print(lengths['82'])
    print(lengths['99'])
    print(lengths['115'])
    print(lengths['133'])
    print(lengths['165'])
    print(lengths['188'])
    print(lengths['197'])
