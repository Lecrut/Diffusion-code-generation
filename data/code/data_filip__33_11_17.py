from collections import deque

def min_steps_to_exit(maze):
    if not maze or not maze[0]:
        return -1

    rows = len(maze)
    cols = len(maze[0])
    
    start = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break
            
    if start is None:
        return -1

    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        if maze[r][c] == 'E':
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
                
    return -1

if __name__ == '__main__':
    sample_maze = [
        ['S', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.'],
        ['#', '#', '#', '#', 'E']
    ]
    print(min_steps_to_exit(sample_maze))