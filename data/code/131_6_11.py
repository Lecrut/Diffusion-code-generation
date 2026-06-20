def has_cycle(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

def detect_cycles(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    rec_stack = [False] * num_nodes

    for node in range(num_nodes):
        if not visited[node]:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False

if __name__ == '__main__':
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    print(detect_cycles(graph))