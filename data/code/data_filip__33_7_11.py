from collections import deque

def shortest_path_grid(grid):
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    start_node = None
    end_node = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                start_node = (r, c)
            elif grid[r][c] == 2:
                end_node = (r, c)
    
    if not start_node or not end_node:
        return -1
    
    queue = deque()
    queue.append((start_node, 0))
    visited = set()
    visited.add(start_node)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        (curr_r, curr_c), dist = queue.popleft()
        
        if (curr_r, curr_c) == end_node:
            return dist
        
        for dr, dc in directions:
            new_r, new_c = curr_r + dr, curr_c + dc
            
            if 0 <= new_r < rows and 0 <= new_c < cols:
                if grid[new_r][new_c] != 1 and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append(((new_r, new_c), dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 2],
        [1, 1, 1, 1]
    ]
    result = shortest_path_grid(sample_grid)
    print(result)