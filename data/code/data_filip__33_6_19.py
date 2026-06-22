import collections
import heapq

def shortest_path_grid(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if rows == 0 or cols == 0:
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    if start == end:
        return [start]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(0, [start])]
    visited = {start}
    while queue:
        dist, path = heapq.heappop(queue)
        curr = path[-1]
        for dr, dc in directions:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                if (nr, nc) == end:
                    return new_path
                visited.add((nr, nc))
                heapq.heappush(queue, (dist + 1, new_path))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    result = shortest_path_grid(sample_grid, start_point, end_point)
    print(result)