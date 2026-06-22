from collections import deque

def minimum_steps_to_exit(grid):
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    start_r, start_c = None, None
    exit_r, exit_c = None, None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start_r, start_c = r, c
            elif grid[r][c] == 3:
                exit_r, exit_c = r, c

    if start_r is None or exit_r is None:
        return -1

    visited = set()
    visited.add((start_r, start_c))
    queue = deque([(start_r, start_c, 0)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        curr_r, curr_c, steps = queue.popleft()

        if curr_r == exit_r and curr_c == exit_c:
            return steps

        for dr, dc in directions:
            next_r, next_c = curr_r + dr, curr_c + dc

            if 0 <= next_r < rows and 0 <= next_c < cols:
                if grid[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                    if grid[next_r][next_c] == 3:
                        return steps + 1
                    visited.add((next_r, next_c))
                    queue.append((next_r, next_c, steps + 1))

    return -1

if __name__ == '__main__':
    maze = [
        [2, 0, 0],
        [0, 1, 0],
        [0, 0, 3]
    ]
    result = minimum_steps_to_exit(maze)
    print(result)