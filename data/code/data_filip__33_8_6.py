from collections import deque

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def find_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    
    sr, sc = start
    er, ec = end
    
    if not is_valid(sr, sc, rows, cols) or grid[sr][sc] == 1:
        return None
    
    if not is_valid(er, ec, rows, cols) or grid[er][ec] == 1:
        return None
    
    if sr == er and sc == ec:
        return [start]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True
    
    queue = deque()
    queue.append((sr, sc, [start]))
    
    while queue:
        r, c, path = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if is_valid(nr, nc, rows, cols) and not visited[nr][nc] and grid[nr][nc] == 0:
                new_path = path + [(nr, nc)]
                
                if nr == er and nc == ec:
                    return new_path
                
                visited[nr][nc] = True
                queue.append((nr, nc, new_path))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_point = (0, 0)
    end_point = (3, 3)
    
    result = find_shortest_path(sample_grid, start_point, end_point)
    print(result)