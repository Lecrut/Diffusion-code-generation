from collections import deque

def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if start == end:
        return 0
    queue = deque([(start, 0)])
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        (r, c), dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                if (nr, nc) == end:
                    return dist + 1
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)
    result = bfs_shortest_path(sample_grid, start_pos, end_pos)
    print(result)