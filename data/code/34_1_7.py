from collections import deque

def bfs_shortest_path(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return -1
    
    start_row, start_col = start
    goal_row, goal_col = goal
    
    if (start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols or
        goal_row < 0 or goal_row >= rows or goal_col < 0 or goal_col >= cols):
        return -1
    
    if grid[start_row][start_col] == 1 or grid[goal_row][goal_col] == 1:
        return -1
    
    if start == goal:
        return 0
    
    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True
    
    queue = deque()
    queue.append((start_row, start_col, 0))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        curr_row, curr_col, dist = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = curr_row + dr, curr_col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                not visited[new_row][new_col] and grid[new_row][new_col] == 0):
                
                if new_row == goal_row and new_col == goal_col:
                    return dist + 1
                
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
    
    return -1

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start_point = (0, 0)
    goal_point = (4, 4)
    
    result = bfs_shortest_path(sample_grid, start_point, goal_point)
    print(result)