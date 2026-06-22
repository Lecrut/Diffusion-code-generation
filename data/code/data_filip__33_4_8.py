from collections import deque

def bidirectional_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    def get_neighbors(pos):
        r, c = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors
    
    if start == end:
        return [start]
    
    if grid[start[0]][start[1]] != 0 or grid[end[0]][end[1]] != 0:
        return None
    
    forward_visited = {start: None}
    backward_visited = {end: None}
    forward_queue = deque([start])
    backward_queue = deque([end])
    
    def intersect():
        for node in forward_visited:
            if node in backward_visited:
                return node
        return None
    
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            current = forward_queue.popleft()
            current_visited = forward_visited
            other_visited = backward_visited
            for neighbor in get_neighbors(current):
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current
                    forward_queue.append(neighbor)
        else:
            current = backward_queue.popleft()
            current_visited = backward_visited
            other_visited = forward_visited
            for neighbor in get_neighbors(current):
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = current
                    backward_queue.append(neighbor)
        
        meeting_point = intersect()
        if meeting_point is not None:
            path_forward = []
            curr = meeting_point
            while curr is not None:
                path_forward.append(curr)
                curr = forward_visited[curr]
            path_forward.reverse()
            
            path_backward = []
            curr = meeting_point
            while curr is not None:
                path_backward.append(curr)
                curr = backward_visited[curr]
            path_backward.reverse()
            
            full_path = path_forward + path_backward[1:]
            return full_path
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs(grid, start, end)
    print(result)