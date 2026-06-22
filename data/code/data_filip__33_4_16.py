import collections

def bidirectional_bfs(start, end, grid, obstacles):
    rows = len(grid)
    cols = len(grid[0])
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#' and (r, c) not in obstacles

    if not is_valid(start[0], start[1]) or not is_valid(end[0], end[1]):
        return None

    if start == end:
        return [start]

    queue_start = collections.deque([start])
    queue_end = collections.deque([end])
    
    visited_start = {start: None}
    visited_end = {end: None}
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def expand(queue, visited, other_visited):
        point = queue.popleft()
        r, c = point
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if neighbor in visited:
                continue
            if not is_valid(nr, nc):
                continue
            
            visited[neighbor] = point
            queue.append(neighbor)
            
            if neighbor in other_visited:
                return neighbor
        return None

    meeting_point = None
    
    while queue_start and queue_end:
        meeting_point = expand(queue_start, visited_start, visited_end)
        if meeting_point:
            break
        
        meeting_point = expand(queue_end, visited_end, visited_start)
        if meeting_point:
            break
            
    if not meeting_point:
        return None

    path_start = []
    curr = meeting_point
    while curr is not None:
        path_start.append(curr)
        curr = visited_start[curr]
    path_start.reverse()
    
    path_end = []
    curr = visited_end[meeting_point]
    while curr is not None:
        path_end.append(curr)
        curr = visited_end.get(curr)
        
    path_start.extend(path_end)
    return path_start

if __name__ == '__main__':
    grid = [
        ['.', '.', '.', '#'],
        ['.', '#', '.', '.'],
        ['.', '.', '.', '.'],
    ]
    obstacles = set()
    start_node = (0, 0)
    end_node = (2, 3)
    
    result = bidirectional_bfs(start_node, end_node, grid, obstacles)
    print(result)