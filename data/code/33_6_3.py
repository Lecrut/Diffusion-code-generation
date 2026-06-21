from collections import deque

def shortest_path(grid):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    if start is None or end is None:
        return -1
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '#':
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

if __name__ == '__main__':
    grid = [
        ['S', '.', '.', '#'],
        ['.', '.', '#', '.'],
        ['.', '.', '.', 'E']
    ]
    result = shortest_path(grid)
    print(result)
    
    grid2 = [
        ['S', '#', 'E']
    ]
    result2 = shortest_path(grid2)
    print(result2)