from collections import deque

def bfs_shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if start == end:
        return [start]
    visited = set()
    visited.add(start)
    queue = deque([(start, [start])])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        current, path = queue.popleft()
        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 0:
                new_path = path + [(nr, nc)]
                if (nr, nc) == end:
                    return new_path
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    return None

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1]
    ]
    start = (0, 0)
    end = (4, 4)
    result = bfs_shortest_path(grid, start, end)
    print(result)