from collections import deque

def bidirectional_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    if start == end:
        return [start]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0
    
    front_visited = {start: None}
    back_visited = {end: None}
    front_queue = deque([start])
    back_queue = deque([end])
    
    meeting_point = None
    
    while front_queue and back_queue:
        if front_queue:
            curr = front_queue.popleft()
            for dr, dc in directions:
                nr, nc = curr[0] + dr, curr[1] + dc
                if is_valid(nr, nc) and (nr, nc) not in front_visited:
                    front_visited[(nr, nc)] = curr
                    front_queue.append((nr, nc))
                    if (nr, nc) in back_visited:
                        meeting_point = (nr, nc)
                        break
            if meeting_point:
                break
        
        if back_queue:
            curr = back_queue.popleft()
            for dr, dc in directions:
                nr, nc = curr[0] + dr, curr[1] + dc
                if is_valid(nr, nc) and (nr, nc) not in back_visited:
                    back_visited[(nr, nc)] = curr
                    back_queue.append((nr, nc))
                    if (nr, nc) in front_visited:
                        meeting_point = (nr, nc)
                        break
            if meeting_point:
                break
    
    if meeting_point is None:
        return None
    
    path_front = []
    node = meeting_point
    while node is not None:
        path_front.append(node)
        node = front_visited[node]
    path_front.reverse()
    
    path_back = []
    node = back_visited[meeting_point]
    while node is not None:
        path_back.append(node)
        node = back_visited[node]
    
    return path_front + path_back

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs(grid, start, end)
    print(result)