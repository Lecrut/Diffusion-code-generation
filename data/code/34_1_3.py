from collections import deque

def bfs_shortest_path(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if not grid or not grid[0]:
        return -1
    
    if start == goal:
        return 0
    
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 0:
                    if (nr, nc) == goal:
                        return dist + 1
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
    
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    result = bfs_shortest_path(grid, start, goal)
    print(result)