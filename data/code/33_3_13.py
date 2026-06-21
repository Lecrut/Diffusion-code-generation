from collections import deque

def shortest_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        (r, c), path = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                new_path = path + [(nr, nc)]
                
                if (nr, nc) == end:
                    return new_path
                
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    result = shortest_path(grid)
    print(result)