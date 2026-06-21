import collections

def find_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if not grid or start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    queue = collections.deque([(start, [start])])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    result = find_shortest_path(sample_grid, start_point, end_point)
    print(result)