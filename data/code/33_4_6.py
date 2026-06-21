import collections

def bidirectional_bfs(grid, start, end):
    if start not in grid or end not in grid:
        return None
    rows = len(grid)
    if rows == 0:
        return None
    cols = len(grid[0])
    if cols == 0:
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    
    front_queue = collections.deque([start])
    back_queue = collections.deque([end])
    front_visited = {start: [start]}
    back_visited = {end: [end]}
    
    while front_queue and back_queue:
        if len(front_queue) <= len(back_queue):
            current_queue, other_visited, other_back_visited = front_queue, back_visited, front_visited
            is_front = True
        else:
            current_queue, other_visited, other_back_visited = back_queue, front_visited, back_visited
            is_front = False
        
        for _ in range(len(current_queue)):
            r, c = current_queue.popleft()
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if (nr, nc) in other_visited:
                        path1 = other_visited[(nr, nc)]
                        path2 = other_back_visited[(r, c)]
                        if is_front:
                            return path1 + path2
                        return path1 + path2[::-1]
                    
                    if (nr, nc) not in other_back_visited:
                        other_back_visited[(nr, nc)] = other_back_visited[(r, c)] + [(nr, nc)]
                        current_queue.append((nr, nc))
    
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
    result = bidirectional_bfs(sample_grid, start_point, end_point)
    print(result)