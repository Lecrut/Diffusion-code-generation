from collections import deque

def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    if start == end:
        return [start]
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (r, c), path = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                if (nr, nc) == end:
                    return new_path
                visited.add((nr, nc))
                queue.append(((nr, nc), new_path))
    return []

if __name__ == '__main__':
    grid_sample = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_sample = (0, 0)
    end_sample = (4, 4)
    result_sample = shortest_path(grid_sample, start_sample, end_sample)
    print(result_sample)