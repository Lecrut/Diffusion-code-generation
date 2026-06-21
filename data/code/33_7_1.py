from collections import deque

def shortest_path(grid):
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
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    grid_data = [
        ['S', '.', '.', '.'],
        ['.', '#', '.', '.'],
        ['.', '.', '#', '.'],
        ['.', '.', '.', 'E']
    ]
    result = shortest_path(grid_data)
    print(result)