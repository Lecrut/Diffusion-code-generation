def shortest_path_binary_matrix(grid):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    if rows == 1 and cols == 1:
        return 1
    queue = [(0, 0, 1)]
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while queue:
        r, c, dist = queue.pop(0)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                if nr == rows - 1 and nc == cols - 1:
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    result = shortest_path_binary_matrix(sample_grid)
    print(result)