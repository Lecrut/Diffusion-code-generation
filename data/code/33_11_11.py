from collections import deque
import heapq

def min_steps_to_exit(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    start_pos = None
    end_pos = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start_pos = (r, c)
            elif grid[r][c] == 3:
                end_pos = (r, c)

    if start_pos is None or end_pos is None:
        return -1

    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = {start_pos}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == end_pos:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

    return -1

if __name__ == '__main__':
    maze = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 2, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 3, 1]
    ]
    result = min_steps_to_exit(maze)
    print(result)