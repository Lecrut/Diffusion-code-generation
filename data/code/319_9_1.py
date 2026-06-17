import collections
def fill_grid_dfs(R, C):
    grid = [[0] * C for _ in range(R)]
    counter = 1
    stack = [(0, 0)]
    visited = set([(0, 0)])
    while stack:
        r, c = stack.pop()
        grid[r][c] = counter
        counter += 1
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append((nr, nc))
    return grid
if __name__ == '__main__':
    R = 3
    C = 4
    result_grid = fill_grid_dfs(R, C)
    for row in result_grid:
        print(row)