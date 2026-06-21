from collections import deque

def shortest_path_grid(grid):
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
    queue = deque([(start[0], start[1], [])])
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c, path = queue.popleft()
        current_path = path + [(r, c)]
        if (r, c) == end:
            return current_path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, current_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#', '.'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', 'E']
    ]
    result = shortest_path_grid(sample_grid)
    print(result)