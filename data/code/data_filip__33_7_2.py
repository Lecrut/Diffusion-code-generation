from collections import deque

def shortest_path_on_grid(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = start
    end_row, end_col = end

    if grid[start_row][start_col] == 1 or grid[end_row][end_col] == 1:
        return -1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start_row, start_col, 0)])
    visited = set((start_row, start_col))

    while queue:
        r, c, dist = queue.popleft()
        if r == end_row and c == end_col:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start = (0, 0)
    end = (2, 3)
    result = shortest_path_on_grid(grid, start, end)
    print(result)