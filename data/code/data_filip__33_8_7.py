from collections import deque

def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    
    if start is None or end is None:
        return None
    
    sr, sc = start
    er, ec = end
    
    if not (0 <= sr < rows and 0 <= sc < cols):
        return None
    if not (0 <= er < rows and 0 <= ec < cols):
        return None
        
    if grid[sr][sc] == 0 or grid[er][ec] == 0:
        return None
    
    queue = deque([(sr, sc, [(sr, sc)])])
    visited = set([(sr, sc)])
    
    while queue:
        r, c, path = queue.popleft()
        
        if r == er and c == ec:
            return path
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    queue.append((nr, nc, new_path))
                    
    return None

if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    result = bfs_shortest_path(grid, start_point, end_point)
    print(result)