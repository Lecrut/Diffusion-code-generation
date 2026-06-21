from collections import deque

def find_shortest_path(grid, start, goal):
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    if cols == 0:
        return -1
    
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    
    if start == goal:
        return 0
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == goal:
                    return dist + 1
                
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
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
    sample_start = (0, 0)
    sample_goal = (4, 4)
    result = find_shortest_path(sample_grid, sample_start, sample_goal)
    print(result)