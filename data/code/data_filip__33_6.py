from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    start = None
    end = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                start = (r, c)
            elif grid[r][c] == 2:
                end = (r, c)
    
    if start is None or end is None:
        return -1
    
    if start == end:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = set()
    visited.add(start)
    queue = deque([(start[0], start[1], 0)])
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == end:
                    return dist + 1
                
                if grid[nr][nc] != 0 or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    grid1 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 2]
    ]
    result1 = shortest_path(grid1)
    print(result1)
    
    grid2 = [
        [1, 0, 1],
        [0, 0, 0],
        [0, 0, 2]
    ]
    result2 = shortest_path(grid2)
    print(result2)
    
    grid3 = [
        [1, 0, 2]
    ]
    result3 = shortest_path(grid3)
    print(result3)