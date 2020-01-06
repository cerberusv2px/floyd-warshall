import time

import src.dataloader as dataloader


def compute(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                temp_distance = graph[i][k] + graph[k][j]
                if temp_distance < graph[i][j]:
                    graph[i][j] = temp_distance
    return graph


def route_path(graph):
    i = 0
    loop_counter = 0
    route_list = []
    route_index = [0]

    while loop_counter < len(graph):
        min_route_index = 0
        min_distance = 9999999.99

        j = 0
        while j < len(graph):
            if i != j:
                if j not in route_index:
                    if min_distance > graph[i][j]:
                        min_distance = graph[i][j]
                        min_route_index = j
            j = j + 1

        if min_route_index not in route_index:
            route_index.append(min_route_index)
            route_list.append("Outlet: %d \t Distance: %f km" % (min_route_index, min_distance))

        i = min_route_index
        loop_counter = loop_counter + 1

    for route in route_list:
        print(route)


def main():
    start_time = time.clock()
    outlets = dataloader.generate_outlets()
    graph = dataloader.get_distance_graph(outlets)
    print(graph)
    new_graph = compute(graph)
    route_path(new_graph)
    print("Total execution time %s seconds" % (time.clock() - start_time))


if __name__ == '__main__':
    main()
