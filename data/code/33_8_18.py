import collections

def validate_grid(grid, rows, cols, start, end):
    if not grid or not isinstance(grid, list):
        return False
    if len(grid) != rows:
        return False
    for row in grid:
        if not isinstance(row, list) or len(row) != cols:
            return False
    sx, sy = start
    ex, ey = end
    if not (0 <= sx < rows and 0 <= sy < cols):
        return False
    if not (0 <= ex < rows and 0 <= ey < cols):
        return False
    if grid[sx][sy] == 1 or grid[ex][ey] == 1:
        return False
    return True

def bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    if not validate_grid(grid, rows, cols, start, end):
        return None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                new_path = path + [(nx, ny)]
                queue.append(((nx, ny), new_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    start_point = (0, 0)
    end_point = (2, 2)
    result = bfs_shortest_path(sample_grid, start_point, end_point)
    print(result)