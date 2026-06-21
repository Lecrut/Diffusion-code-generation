import collections

def find_shortest_path(grid):
    if not grid or not grid[0]:
        return None
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
        return None
    queue = collections.deque([start])
    visited = {start: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        curr_r, curr_c = queue.popleft()
        if (curr_r, curr_c) == end:
            path = []
            current = end
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(start)
            return list(reversed(path))
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X' and (nr, nc) not in visited:
                visited[(nr, nc)] = (curr_r, curr_c)
                queue.append((nr, nc))
    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', 'X'],
        ['X', '.', 'X', '.'],
        ['.', '.', 'X', 'E'],
        ['X', '.', '.', '.']
    ]
    result = find_shortest_path(sample_grid)
    print(result)