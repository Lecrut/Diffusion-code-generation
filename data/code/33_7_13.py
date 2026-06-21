from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    start = (0, 0)
    end = (rows - 1, cols - 1)

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    queue = deque([(start, 0)])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (r, c), dist = queue.popleft()

        if r == end[0] and c == end[1]:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append(((nr, nc), dist + 1))

    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    result = shortest_path(sample_grid)
    print(result)