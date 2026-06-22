import collections

def bidirectional_bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return []
    
    if start == end:
        return [start]
    
    def get_neighbors(pos):
        r, c = pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                neighbors.append((nr, nc))
        return neighbors
    
    queue_start = collections.deque([start])
    queue_end = collections.deque([end])
    
    visited_start = {start: None}
    visited_end = {end: None}
    
    meeting_point = None
    
    while queue_start and queue_end:
        if len(queue_start) <= len(queue_end):
            meeting_point = expand_frontier(
                queue_start, visited_start, visited_end, grid
            )
        else:
            meeting_point = expand_frontier(
                queue_end, visited_end, visited_start, grid
            )
        
        if meeting_point is not None:
            break
    
    if meeting_point is None:
        return []
    
    path = reconstruct_path(visited_start, visited_end, meeting_point)
    return path

def expand_frontier(queue, current_visited, other_visited, grid):
    if not queue:
        return None
    
    pos = queue.popleft()
    neighbors = get_neighbors_for_expand(pos, grid)
    
    for neighbor in neighbors:
        if neighbor in other_visited:
            return neighbor
        
        if neighbor not in current_visited:
            current_visited[neighbor] = pos
            queue.append(neighbor)
    
    return None

def get_neighbors_for_expand(pos, grid):
    r, c = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
            neighbors.append((nr, nc))
    
    return neighbors

def reconstruct_path(visited_start, visited_end, meeting_point):
    path_from_start = []
    current = meeting_point
    
    while current is not None:
        path_from_start.append(current)
        current = visited_start[current]
    
    path_from_start.reverse()
    
    path_from_end = []
    current = visited_end[meeting_point]
    
    while current is not None:
        path_from_end.append(current)
        current = visited_end[current]
    
    return path_from_start + path_from_end

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    
    start_pos = (0, 0)
    end_pos = (4, 4)
    
    result_path = bidirectional_bfs_shortest_path(grid, start_pos, end_pos)
    print(result_path)