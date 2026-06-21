import collections

def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    if start == end:
        return [start]
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    
    queue = collections.deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    if (nr, nc) == end:
                        return new_path
                    queue.append(((nr, nc), new_path))
    
    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_node = (0, 0)
    end_node = (2, 3)
    result = shortest_path(sample_grid, start_node, end_node)
    print(result)