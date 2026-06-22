from collections import deque

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    if rows == 1 and cols == 1:
        return 1
    
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if nr == rows - 1 and nc == cols - 1:
                    return dist + 1
                
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    result = shortest_path_binary_matrix(sample_grid)
    print(result)
    
    sample_grid_2 = [
        [0, 1],
        [1, 0]
    ]
    result_2 = shortest_path_binary_matrix(sample_grid_2)
    print(result_2)
    
    sample_grid_3 = [[0]]
    result_3 = shortest_path_binary_matrix(sample_grid_3)
    print(result_3)