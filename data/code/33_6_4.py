from collections import deque

def shortest_path(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return -1
    
    start = None
    end = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    
    if start is None or end is None:
        return -1
    
    queue = deque([(start, 0)])
    visited = {start}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        list('S..'),
        list('.#.'),
        list('..E')
    ]
    result = shortest_path(sample_grid)
    print(result)
    
    sample_grid_2 = [
        list('S#'),
        list('#E')
    ]
    result_2 = shortest_path(sample_grid_2)
    print(result_2)
    
    sample_grid_3 = [
        list('SE')
    ]
    result_3 = shortest_path(sample_grid_3)
    print(result_3)