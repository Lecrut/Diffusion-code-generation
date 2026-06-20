def has_cycle(graph, node, visited, stack):
    if node in stack:
        return True
    if node in visited:
        return False
    visited.add(node)
    stack.add(node)
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visited, stack):
            return True
    stack.remove(node)
    return False

def detect_cycles(graph):
    visited = set()
    stack = set()
    for node in graph:
        if node not in visited and has_cycle(graph, node, visited, stack):
            return True
    return False
if __name__ == '__main__':
    sample_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['F'], 'D': ['E'], 'E': [], 'F': ['D']}
    print(detect_cycles(sample_graph))