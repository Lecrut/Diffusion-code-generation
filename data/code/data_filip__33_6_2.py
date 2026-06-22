from collections import deque

def shortest_path(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    start_r, start_c = 0, 0
    end_r, end_c = rows - 1, cols - 1
    
    if grid[start_r][start_c] != 0 or grid[end_r][end_c] != 0:
        return -1
    
    if rows == 1 and cols == 1:
        return 0
    
    visited = [[False] * cols for _ in range(rows)]
    visited[start_r][start_c] = True
    queue = deque([(start_r, start_c, 0)])
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                if nr == end_r and nc == end_c:
                    return dist + 1
                
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return -1

if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ]
    
    result = shortest_path(grid)
    print(result)