def find_shortest_path_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []

    queue = [[start, [start]]]
    visited = set()
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current, path = queue.pop(0)

        if current == end:
            return path

        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in visited:
                visited.add((r, c))
                new_path = list(path)
                new_path.append((r, c))
                queue.append(((r, c), new_path))

    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    path = find_shortest_path_bfs(sample_grid)
    print(path)