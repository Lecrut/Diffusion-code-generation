from collections import deque

def bidirectional_bfs(grid, start, goal):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return None
    if goal[0] < 0 or goal[0] >= rows or goal[1] < 0 or goal[1] >= cols:
        return None
    if grid[start[0]][start[1]] == 1:
        return None
    if grid[goal[0]][goal[1]] == 1:
        return None
    if start == goal:
        return [start]
    
    start_queue = deque([start])
    goal_queue = deque([goal])
    start_visited = {start: None}
    goal_visited = {goal: None}
    
    while start_queue and goal_queue:
        if len(start_queue) <= len(goal_queue):
            current = start_queue.popleft()
            r, c = current
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 0:
                        if (nr, nc) not in start_visited:
                            start_visited[(nr, nc)] = current
                            start_queue.append((nr, nc))
                            if (nr, nc) in goal_visited:
                                path = reconstruct_path(start_visited, goal_visited, (nr, nc))
                                return path
        else:
            current = goal_queue.popleft()
            r, c = current
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 0:
                        if (nr, nc) not in goal_visited:
                            goal_visited[(nr, nc)] = current
                            goal_queue.append((nr, nc))
                            if (nr, nc) in start_visited:
                                path = reconstruct_path(start_visited, goal_visited, (nr, nc))
                                return path
    return None

def reconstruct_path(start_visited, goal_visited, meeting_point):
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = start_visited[current]
    path.reverse()
    current = goal_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = goal_visited[current]
    return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    goal_node = (4, 4)
    result = bidirectional_bfs(grid, start_node, goal_node)
    print(result)
    print(f"Path length: {len(result) - 1 if result else 0}")