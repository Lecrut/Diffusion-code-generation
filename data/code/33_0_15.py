from collections import deque

def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque([(start, [start])])
    visited = set([start])
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
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_pos = (0, 0)
    end_pos = (3, 3)
    path = bfs_shortest_path(sample_grid, start_pos, end_pos)
    print(path)