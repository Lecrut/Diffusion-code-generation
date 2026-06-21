from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 0 or grid[rows - 1][cols - 1] == 0:
        return -1

    visited = set()
    visited.add((0, 0))
    queue = deque([(0, 0, 0)])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        if r == rows - 1 and c == cols - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    grid_data = [
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 1]
    ]

    result = shortest_path(grid_data)
    print(result)