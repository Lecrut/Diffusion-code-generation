from collections import deque
from typing import List, Tuple

def min_steps_to_exit(maze: List[List[int]]) -> int:
    if not maze or not maze[0]:
        return -1
    
    rows = len(maze)
    cols = len(maze[0])
    
    start = None
    exit_pos = None
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                start = (r, c)
            elif maze[r][c] == 2:
                exit_pos = (r, c)
    
    if start is None or exit_pos is None:
        return -1
    
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        if (r, c) == exit_pos:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if maze[nr][nc] != 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))
    
    return -1

if __name__ == '__main__':
    maze = [
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 2],
        [0, 0, 0, 1]
    ]
    result = min_steps_to_exit(maze)
    print(result)