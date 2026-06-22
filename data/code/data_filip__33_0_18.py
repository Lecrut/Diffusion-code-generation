import collections

def find_shortest_path_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    queue = collections.deque([(start, [start])])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    result = find_shortest_path_bfs(grid, start, end)
    print(result)