import collections

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
    
    sr, sc = start
    er, ec = end
    
    if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
        return None
    if er < 0 or er >= rows or ec < 0 or ec >= cols:
        return None
        
    if grid[sr][sc] != 'S' or grid[er][ec] != 'E':
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = collections.deque([(sr, sc, [])])
    visited = set()
    visited.add((sr, sc))
    
    while queue:
        r, c, path = queue.popleft()
        
        if (r, c) == (er, ec):
            return path + [(r, c)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != '#':
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [(r, c)]))
                    
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#'],
        ['.', '.', '.', '.'],
        ['.', '#', '.', 'E'],
        ['.', '.', '.', '.']
    ]
    
    result = find_shortest_path(sample_grid)
    print(result)