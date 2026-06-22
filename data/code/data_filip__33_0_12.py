from collections import deque

def shortest_path_grid(grid):
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
        return []
    
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current_pos, path = queue.popleft()
        
        if current_pos == end:
            return path
        
        r, c = current_pos
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]
                if cell != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append(((nr, nc), new_path))
    
    return []

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#'],
        ['.', '#', '.', '.'],
        ['.', '.', '.', 'E']
    ]
    
    result = shortest_path_grid(sample_grid)
    print(result)