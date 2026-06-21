from collections import deque

def find_shortest_path(grid):
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    start = None
    goal = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'G':
                goal = (r, c)
    
    if start is None or goal is None:
        return -1
    
    queue = deque([start])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            return grid[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X' and (nr, nc) not in visited:
                visited.add((nr, nc))
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', 'X', 'G'],
        ['X', '.', 'X', '.', '.'],
        ['.', '.', '.', 'X', '.'],
        ['.', 'X', '.', '.', '.'],
        ['.', '.', '.', 'X', '.']
    ]
    
    for i in range(len(sample_grid)):
        for j in range(len(sample_grid[0])):
            if sample_grid[i][j] == 'S':
                sample_grid[i][j] = 0
            elif sample_grid[i][j] == '.':
                sample_grid[i][j] = 0
    
    result = find_shortest_path(sample_grid)
    print(result)