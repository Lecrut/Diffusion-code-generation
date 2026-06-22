from collections import deque

def solve_maze_bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == goal:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start_point = (0, 0)
    goal_point = (4, 4)
    result = solve_maze_bfs(sample_grid, start_point, goal_point)
    print(result)