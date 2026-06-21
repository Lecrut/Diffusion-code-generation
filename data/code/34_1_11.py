from collections import deque

def solve_grid_maze(maze):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    
    start = None
    goal = None
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'G':
                goal = (r, c)
                
    if start is None or goal is None:
        return -1
        
    queue = deque([(start, 0)])
    visited = set([start])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == goal:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and maze[nr][nc] != '#':
                    if (nr, nc) == goal:
                        return dist + 1
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
                    
    return -1

if __name__ == '__main__':
    maze_example = [
        ['S', '.', '.', '#'],
        ['#', '.', '.', '.'],
        ['.', '.', '.', 'G']
    ]
    
    result = solve_grid_maze(maze_example)
    print(result)