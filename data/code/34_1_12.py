from collections import deque

def bfs_path_length(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or grid[start[0]][start[1]] == 1:
        return -1
    if goal[0] < 0 or goal[0] >= rows or goal[1] < 0 or goal[1] >= cols or grid[goal[0]][goal[1]] == 1:
        return -1
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == goal:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    sample_start = (0, 0)
    sample_goal = (4, 4)
    result = bfs_path_length(sample_grid, sample_start, sample_goal)
    print(result)