from collections import deque

def min_steps_to_exit(maze):
    if not maze or not maze[0]:
        return -1

    rows = len(maze)
    cols = len(maze[0])

    start_pos = None
    exit_pos = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_pos = (r, c)
            elif maze[r][c] == 'E':
                exit_pos = (r, c)

    if start_pos is None or exit_pos is None:
        return -1

    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = set()
    visited.add(start_pos)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == exit_pos:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

    return -1

if __name__ == '__main__':
    sample_maze = [
        ['S', '.', '.', '#'],
        ['#', '#', '.', '.'],
        ['.', '.', 'E', '#'],
        ['#', '#', '.', '.']
    ]
    print(min_steps_to_exit(sample_maze))