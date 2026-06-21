from collections import deque

def find_shortest_path(grid):
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    
    if start is None or end is None:
        return None
    
    queue = deque([(start, [start])])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != 'X':
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '0', '0', '0', '0'],
        ['0', 'X', 'X', 'X', '0'],
        ['0', '0', '0', 'X', '0'],
        ['X', 'X', '0', '0', '0'],
        ['0', '0', '0', 'X', 'E']
    ]
    
    result = find_shortest_path(sample_grid)
    print(result)