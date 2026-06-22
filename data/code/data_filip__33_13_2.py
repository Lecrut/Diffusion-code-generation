from collections import deque

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0]:
        return 0
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    rows = len(grid)
    cols = len(grid[0])
    if rows == 1 and cols == 1:
        return 1

    queue = deque([(0, 0, 1)])
    grid[0][0] = 1

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    grid1 = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]
    print(shortest_path_binary_matrix(grid1))

    grid2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortest_path_binary_matrix(grid2))

    grid3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(shortest_path_binary_matrix(grid3))