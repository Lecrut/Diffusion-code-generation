from collections import deque

def shortest_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    if grid[0][0] == 0 or grid[rows - 1][cols - 1] == 0:
        return -1
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    grid = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(shortest_path(grid))