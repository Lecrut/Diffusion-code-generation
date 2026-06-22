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
    if start is None or end is None:
        return None
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#'],
        ['#', '.', '#', '.'],
        ['.', '.', '.', 'E'],
        ['#', '#', '#', '#']
    ]
    result = shortest_path(sample_grid)
    print(result)