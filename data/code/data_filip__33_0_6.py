def shortest_path_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = [(0, 0, 1)]
    visited = set()
    visited.add((0, 0))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        r, c, dist = queue.pop(0)
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result = shortest_path_bfs(grid)
    print(result)