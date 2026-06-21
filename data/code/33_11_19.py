from collections import deque

def min_steps_to_exit(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = None
    exit_pos = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                exit_pos = (r, c)
                
    if start is None or exit_pos is None:
        return -1
        
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), steps = queue.popleft()
        
        if (r, c) == exit_pos:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != '#':
                    if (nr, nc) == exit_pos:
                        return steps + 1
                    visited.add((nr, nc))
                    queue.append(((nr, nc), steps + 1))
                    
    return -1

if __name__ == '__main__':
    maze = [
        ['S', '.', '.', '#'],
        ['#', '.', '.', '.'],
        ['.', '.', '.', 'E']
    ]
    result = min_steps_to_exit(maze)
    print(result)