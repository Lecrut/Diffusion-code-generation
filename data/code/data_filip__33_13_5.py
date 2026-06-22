from collections import deque

def shortest_path_binary_matrix(grid):
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    n = len(grid)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == n - 1 and c == n - 1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortest_path_binary_matrix(sample_grid))