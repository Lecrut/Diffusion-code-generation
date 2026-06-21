from collections import deque

def shortest_path_grid(grid):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    start_val = 0
    end_val = 2
    start_pos = None
    end_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == start_val:
                start_pos = (r, c)
            elif grid[r][c] == end_val:
                end_pos = (r, c)
    if start_pos is None or end_pos is None:
        return None
    queue = deque([start_pos])
    visited = set([start_pos])
    distance = {start_pos: 0}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c = queue.popleft()
        if (r, c) == end_pos:
            return distance[(r, c)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    distance[(nr, nc)] = distance[(r, c)] + 1
                    queue.append((nr, nc))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 2]
    ]
    result = shortest_path_grid(sample_grid)
    print(result)