from collections import deque

def bidirectional_bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return None
    
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    if start == end:
        return [start]
    
    forward_queue = deque([start])
    forward_parent = {start: None}
    
    backward_queue = deque([end])
    backward_parent = {end: None}
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    intersection_node = None
    
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            current_queue = forward_queue
            current_parent = forward_parent
            other_parent = backward_parent
        else:
            current_queue = backward_queue
            current_parent = backward_parent
            other_parent = forward_parent
        
        level_size = len(current_queue)
        for _ in range(level_size):
            curr = current_queue.popleft()
            
            if curr in other_parent:
                intersection_node = curr
                break
            
            for dr, dc in directions:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in current_parent:
                    current_parent[(nr, nc)] = curr
                    current_queue.append((nr, nc))
        
        if intersection_node is not None:
            break
    
    if intersection_node is None:
        return None
    
    path = []
    curr = intersection_node
    while curr is not None:
        path.append(curr)
        curr = forward_parent.get(curr)
    forward_path = list(reversed(path))
    
    curr = intersection_node
    while curr is not None:
        path.append(curr)
        curr = backward_parent.get(curr)
    backward_path = path[1:]
    
    return forward_path + backward_path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs_shortest_path(grid, start, end)
    print(result)