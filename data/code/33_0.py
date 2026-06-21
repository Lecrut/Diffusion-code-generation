from collections import deque

def shortest_path_bfs(grid):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    print(shortest_path_bfs(sample_grid))