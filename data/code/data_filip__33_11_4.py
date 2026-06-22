from collections import deque

def minimum_steps_to_exit(maze):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    start = None
    exit_positions = []

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                exit_positions.append((r, c))

    if start is None:
        return -1

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) in exit_positions:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and maze[nr][nc] != '#':
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    maze = [
        ['S', '.', '#'],
        ['.', '.', '.'],
        ['.', '.', 'E']
    ]
    result = minimum_steps_to_exit(maze)
    print(result)