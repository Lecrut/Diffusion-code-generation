from collections import deque

def bidirectional_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    if start == end:
        return [start]
    
    forward_visited = {start: None}
    backward_visited = {end: None}
    
    forward_queue = deque([start])
    backward_queue = deque([end])
    
    def get_neighbors(pos):
        x, y = pos
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors
    
    meeting_point = None
    
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            current = forward_queue.popleft()
            neighbors = get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current
                    forward_queue.append(neighbor)
                    if neighbor in backward_visited:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
        else:
            current = backward_queue.popleft()
            neighbors = get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = current
                    backward_queue.append(neighbor)
                    if neighbor in forward_visited:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
    
    if not meeting_point:
        return None
    
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = forward_visited[current]
    path.reverse()
    
    current = backward_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = backward_visited[current]
    
    return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs(grid, start, end)
    print(result)