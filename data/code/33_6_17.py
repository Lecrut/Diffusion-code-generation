from collections import deque
from typing import List, Tuple, Optional

def shortest_path(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    if rows == 0 or cols == 0:
        return -1
    
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    if rows == 1 and cols == 1:
        return 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    visited.add((0, 0))
    queue = deque([(0, 0, 0)])
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    if nr == rows - 1 and nc == cols - 1:
                        return dist + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)