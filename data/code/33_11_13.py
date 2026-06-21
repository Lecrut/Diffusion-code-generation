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

    queue = deque()
    queue.append((start_pos, 0))
    visited = set()
    visited.add(start_pos)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (current_r, current_c), steps = queue.popleft()

        if (current_r, current_c) == exit_pos:
            return steps

        for dr, dc in directions:
            next_r, next_c = current_r + dr, current_c + dc

            if 0 <= next_r < rows and 0 <= next_c < cols:
                if maze[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    queue.append(((next_r, next_c), steps + 1))

    return -1

if __name__ == '__main__':
    sample_maze = [
        ['S', '.', '.', '#', '.'],
        ['#', '#', '.', '.', '.'],
        ['.', '.', '#', '#', '.'],
        ['.', '.', '.', '.', 'E']
    ]
    result = min_steps_to_exit(sample_maze)
    print(result)