from collections import deque

def bfs_path_length(grid, start, goal):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return -1
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
        return -1
    if grid[start[0]][start[1]] == 1:
        return -1
    if grid[goal[0]][goal[1]] == 1:
        return -1
    if start == goal:
        return 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add((start[0], start[1]))
    queue = deque()
    queue.append((start[0], start[1], 0))
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    if grid[nr][nc] == 0:
                        if (nr, nc) == (goal[0], goal[1]):
                            return dist + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))
    return -1
if __name__ == '__main__':
    grid_sample = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    start_sample = (0, 0)
    goal_sample = (4, 4)
    result = bfs_path_length(grid_sample, start_sample, goal_sample)
    print(result)