from collections import deque

def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return []
    
    if start == end:
        return [start]
    
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return []
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return []
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current, path = queue.popleft()
        
        for dr, dc in directions:
            next_row, next_col = current[0] + dr, current[1] + dc
            next_pos = (next_row, next_col)
            
            if next_pos == end:
                return path + [next_pos]
            
            if (0 <= next_row < rows and 0 <= next_col < cols
                and grid[next_row][next_col] == 0
                and next_pos not in visited):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))
    
    return []

if __name__ == '__main__':
    grid_example = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0]
    ]
    start_pos = (0, 0)
    end_pos = (3, 3)
    path = bfs_shortest_path(grid_example, start_pos, end_pos)
    print(path)
    
    grid_small = [
        [0, 0],
        [0, 0]
    ]
    path2 = bfs_shortest_path(grid_small, (0, 0), (1, 1))
    print(path2)
    
    grid_blocked = [
        [0, 1],
        [1, 0]
    ]
    path3 = bfs_shortest_path(grid_blocked, (0, 0), (1, 1))
    print(path3)
    
    grid_same = [
        [0, 1],
        [1, 0]
    ]
    path4 = bfs_shortest_path(grid_same, (0, 0), (0, 0))
    print(path4)