from collections import deque

def solve_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return None
        
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start point out of grid boundaries")
        
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError("End point out of grid boundaries")
        
    if grid[start[0]][start[1]] == 1:
        raise ValueError("Start point is blocked")
        
    if grid[end[0]][end[1]] == 1:
        raise ValueError("End point is blocked")
        
    visited = set()
    visited.add(start)
    queue = deque([(start, [start])])
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), new_path))
                
    return None

if __name__ == '__main__':
    grid_sample = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_point = (0, 0)
    end_point = (3, 3)
    result = solve_shortest_path(grid_sample, start_point, end_point)
    print(result)