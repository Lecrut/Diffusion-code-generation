import collections

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def bfs_shortest_path(grid, start, end):
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
    
    if start == end:
        return [start]
    
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (curr_r, curr_c), path = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            if is_valid(nr, nc, rows, cols) and (nr, nc) not in visited and grid[nr][nc] == 0:
                new_path = path + [(nr, nc)]
                
                if (nr, nc) == end:
                    return new_path
                
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0]
    ]
    
    sample_start = (0, 0)
    sample_end = (3, 4)
    
    result = bfs_shortest_path(sample_grid, sample_start, sample_end)
    print(result)