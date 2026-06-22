import collections

def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1

def bidirectional_bfs(grid, start, end):
    if not is_valid(grid, start[0], start[1]) or not is_valid(grid, end[0], end[1]):
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    if start == end:
        return [start]
    
    forward_queue = collections.deque([(start, [start])])
    backward_queue = collections.deque([(end, [end])])
    forward_visited = {start: [start]}
    backward_visited = {end: [end]}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            current_queue = forward_queue
            current_visited = forward_visited
            other_visited = backward_visited
            directions_to_check = directions
        else:
            current_queue = backward_queue
            current_visited = backward_visited
            other_visited = forward_visited
            directions_to_check = directions
        
        for _ in range(len(current_queue)):
            (x, y), path = current_queue.popleft()
            
            for dx, dy in directions_to_check:
                nx, ny = x + dx, y + dy
                if is_valid(grid, nx, ny) and (nx, ny) not in current_visited:
                    new_path = path + [(nx, ny)] if current_queue is forward_queue else [(nx, ny)] + path
                    current_visited[(nx, ny)] = new_path
                    current_queue.append(((nx, ny), new_path))
                    
                    if (nx, ny) in other_visited:
                        if current_queue is forward_queue:
                            full_path = new_path[:-1] + other_visited[(nx, ny)][::-1]
                        else:
                            full_path = other_visited[(nx, ny)][::-1] + new_path
                        return full_path
    
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    
    result = bidirectional_bfs(sample_grid, start_point, end_point)
    print(result)