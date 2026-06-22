from collections import deque

def bidirectional_bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    if start == goal:
        return [start]
    
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None
    
    def get_neighbors(pos):
        r, c = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors
    
    visited_start = {start: None}
    visited_goal = {goal: None}
    
    queue_start = deque([start])
    queue_goal = deque([goal])
    
    meeting_point = None
    
    while queue_start and queue_goal:
        if queue_start:
            current = queue_start.popleft()
            for neighbor in get_neighbors(current):
                if neighbor not in visited_start:
                    visited_start[neighbor] = current
                    queue_start.append(neighbor)
                    if neighbor in visited_goal:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
        
        if queue_goal and not meeting_point:
            current = queue_goal.popleft()
            for neighbor in get_neighbors(current):
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = current
                    queue_goal.append(neighbor)
                    if neighbor in visited_start:
                        meeting_point = neighbor
                        break
            if meeting_point:
                break
    
    if not meeting_point:
        return None
    
    path_start = []
    node = meeting_point
    while node is not None:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()
    
    path_goal = []
    node = meeting_point
    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]
    
    return path_start + path_goal[1:]

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    goal_point = (4, 4)
    result_path = bidirectional_bfs(sample_grid, start_point, goal_point)
    print(result_path)