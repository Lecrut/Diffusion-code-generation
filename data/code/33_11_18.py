from collections import deque

def bfs_min_steps(grid):
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
    queue = deque([(start, 0)])
    visited = {start}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        (r, c), steps = queue.popleft()
        if (r, c) == exit_pos:
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), steps + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', 'X', '.'],
        ['X', 'X', '.', '.', '.'],
        ['.', '.', '.', '.', 'E']
    ]
    result = bfs_min_steps(sample_grid)
    print(result)