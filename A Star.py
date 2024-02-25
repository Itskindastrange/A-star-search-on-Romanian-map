import heapq
import math
import matplotlib.pyplot as plt

def plot_path(path, shortest_distances):

    x_values = [coordinates_of_RomanianCities[city][0] for city in path]
    y_values = [coordinates_of_RomanianCities[city][1] for city in path]

    plt.scatter(x_values, y_values, color='blue', label='Cities')
    plt.plot(x_values, y_values, color='red', linestyle='-', marker='o', markersize=5, label='Path')

    for city, (x, y) in coordinates_of_RomanianCities.items():
        plt.annotate(city, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    for (city1, city2), distance in shortest_distances.items():
        x1, y1 = coordinates_of_RomanianCities[city1]
        x2, y2 = coordinates_of_RomanianCities[city2]
        plt.plot([x1, x2], [y1, y2], color='green', linestyle='--')
        plt.text((x1 + x2) / 2, (y1 + y2) / 2, str(distance), fontsize=8)

    plt.title('Shortest Path and Distances between Cities')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()

    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += Romania[path[i]][path[i + 1]]
    return dist

def heuristicFun(current, goal):
    x1, y1 = coordinates_of_RomanianCities[current]
    x2, y2 = coordinates_of_RomanianCities[goal]
    h = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return h

def g(graph, start):
    g = {}
    for i in graph:
        g[i] = float("inf")
    g[start] = 0
    return g

def A_Star(graph, start, goal):
    searchList = [(0, start)]
    checked = set()
    gVal = g(graph, start)
    pNode = {}
    pNode[start] = None

    while searchList:
        currentScore, currentNode = heapq.heappop(searchList)
        if currentNode == goal:
            path = []
            while currentNode:
                path.append(currentNode)
                currentNode = pNode[currentNode]
            return path[::-1]
        checked.add(currentNode)

        for i, j in graph[currentNode].items():
            if i in checked:
                continue
            temp_g = gVal[currentNode] + j

            if gVal[i] > temp_g:
                pNode[i] = currentNode
                gVal[i] = temp_g
                g_and_h_combined = temp_g + heuristicFun(i, goal)
                heapq.heappush(searchList, (g_and_h_combined, i))

    return None

Romania = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

coordinates_of_RomanianCities = {
    'Arad': (46.18656, 21.31227),
    'Bucharest': (44.4268, 25.2838),
    'Craiova': (44.3302, 23.7949),
    'Drobeta': (44.6269, 22.6619),
    'Eforie': (44.0596, 28.6520),
    'Fagaras': (45.8416, 24.9740),
    'Giurgiu': (43.9037, 25.9716),
    'Hirsova': (44.6894, 27.9455),
    'Iasi': (47.1585, 27.5925),
    'Lugoj': (45.6867, 22.4340),
    'Mehadia': (44.9041, 22.3582),
    'Neamt': (46.9759, 26.3813),
    'Oradea': (47.0458, 21.9189),
    'Pitesti': (44.8565, 24.8696),
    'Rimnicu Vilcea': (45.1042, 24.3575),
    'Sibiu': (45.7983, 24.1477),
    'Timisoara': (45.7489, 21.2287),
    'Urziceni': (44.7180, 26.6414),
    'Vaslui': (46.6403, 27.7276),
    'Zerind': (46.6225, 21.7217)
}
shortest_distances = {('Arad', 'Sibiu'): 140, ('Sibiu', 'Rimnicu Vilcea'): 80, ('Rimnicu Vilcea', 'Pitesti'): 97, ('Pitesti', 'Bucharest'): 101}
start=input("Enter start city: ")
goal=input("Enter end city: ")
start=start.capitalize()
goal=goal.capitalize()
#print(start," ",goal)
x=A_Star(Romania,start,goal)
if x:
    print(f"Path from {start} to {goal} : ",x)
    print("Total distance: ",distance(x))
else:
    print("No Path found")

plot_path(x,shortest_distances)
