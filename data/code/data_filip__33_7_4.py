from collections import deque

def shortest_path(grid):
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
    
    if not start or not end:
        return None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != '#':
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append(((nr, nc), new_path))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.'],
        ['.', '.', '#', 'E', '.'],
        ['#', '.', '.', '#', '.']
    ]
    
    result = shortest_path(sample_grid)
    print(result)