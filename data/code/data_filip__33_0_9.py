from collections import deque

def find_shortest_path_bfs(grid):
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
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 'X':
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

if __name__ == '__main__':
    grid_data = [
        ['S', '.', '.', 'X'],
        ['X', 'X', '.', '.'],
        ['.', '.', '.', 'E']
    ]
    result_path = find_shortest_path_bfs(grid_data)
    print(result_path)