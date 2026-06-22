from collections import deque

def bidirectional_bfs(grid, start, end):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    if start == end:
        return [start]

    def get_neighbors(pos):
        r, c = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 0):
                neighbors.append((nr, nc))
        return neighbors
    forward_queue = deque()
    forward_queue.append(start)
    forward_visited = {start: None}
    backward_queue = deque()
    backward_queue.append(end)
    backward_visited = {end: None}
    meeting_point = None
    while forward_queue and backward_queue:
        if forward_queue:
            forward_node = forward_queue.popleft()
            for neighbor in get_neighbors(forward_node):
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = forward_node
                    forward_queue.append(neighbor)
                    if neighbor in backward_visited:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
        if backward_queue:
            backward_node = backward_queue.popleft()
            for neighbor in get_neighbors(backward_node):
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = backward_node
                    backward_queue.append(neighbor)
                    if neighbor in forward_visited:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
    if meeting_point is None:
        return []
    path_forward = []
    current = meeting_point
    while current is not None:
        path_forward.append(current)
        current = forward_visited.get(current)
    path_forward.reverse()
    path_backward = []
    current = meeting_point
    current = backward_visited[meeting_point]
    while current is not None:
        path_backward.append(current)
        current = backward_visited.get(current)
    path = path_forward + path_backward
    return path
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs(grid, start, end)
    print(result)