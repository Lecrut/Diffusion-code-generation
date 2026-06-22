import collections

def shortest_path(grid):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                if start is None:
                    start = (r, c)
                end = (r, c)
    if start is None or end is None:
        return None
    queue = collections.deque([start])
    visited = {start}
    parent_map = {start: None}
    while queue:
        curr = queue.popleft()
        if curr == end:
            break
        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent_map[(nr, nc)] = curr
                    queue.append((nr, nc))
    if end not in parent_map:
        return None
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]
    path.reverse()
    return path

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)