from collections import deque

def find_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        raise ValueError("Grid is empty")

    sr, sc = start
    er, ec = end

    if not (0 <= sr < rows and 0 <= sc < cols):
        raise ValueError("Start point out of bounds")

    if not (0 <= er < rows and 0 <= ec < cols):
        raise ValueError("End point out of bounds")

    if grid[sr][sc] == 0:
        raise ValueError("Start point is blocked")

    if grid[er][ec] == 0:
        raise ValueError("End point is blocked")

    if start == end:
        return 0

    visited = set()
    visited.add(start)
    queue = deque([(start, 1)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (curr_r, curr_c), dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == end:
                    return dist + 1
                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))

    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    sample_start = (0, 0)
    sample_end = (3, 3)

    result = find_shortest_path(sample_grid, sample_start, sample_end)
    print(result)