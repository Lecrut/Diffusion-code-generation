from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return []
    
    if rows == 1 and cols == 1:
        return [start]
    
    queue = deque()
    queue.append((0, 0, [(0, 0)]))
    visited = set()
    visited.add((0, 0))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, path = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    new_path = path + [(nr, nc)]
                    
                    if nr == rows - 1 and nc == cols - 1:
                        return new_path
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc, new_path))
    
    return []

if __name__ == '__main__':
    grid_example = [
        [0, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    
    result = shortest_path(grid_example)
    print(result)