from collections import deque

def bfs_grid_path(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return -1
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
        return -1
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == goal:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    result = bfs_grid_path(sample_grid, start_node, goal_node)
    print(result)