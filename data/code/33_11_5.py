import collections

def min_steps_to_exit(maze, start, end):
    if not maze or not maze[0]:
        return -1
    rows = len(maze)
    cols = len(maze[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return -1
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return -1
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return -1
    queue = collections.deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == end:
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and maze[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
    return -1

if __name__ == '__main__':
    sample_maze = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start_point = (0, 0)
    exit_point = (4, 4)
    result = min_steps_to_exit(sample_maze, start_point, exit_point)
    print(result)