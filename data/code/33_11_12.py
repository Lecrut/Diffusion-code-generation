from collections import deque

def minimum_steps_to_exit(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    start = None
    end = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                end = (r, c)
            elif grid[r][c] == 1:
                start = (r, c)
    
    if start is None or end is None:
        return -1
    
    visited = set()
    visited.add(start)
    queue = deque([(start[0], start[1], 0)])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 2]
    ]
    
    result = minimum_steps_to_exit(grid)
    print(result)