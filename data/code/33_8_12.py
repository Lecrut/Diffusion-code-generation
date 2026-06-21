import collections
import sys

def validate_grid(grid, start, end):
    if not grid or not grid[0]:
        return False, "Grid is empty"
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return False, f"Start point {start} is out of bounds"
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return False, f"End point {end} is out of bounds"
    if grid[start[0]][start[1]] == 1:
        return False, "Start point is blocked"
    if grid[end[0]][end[1]] == 1:
        return False, "End point is blocked"
    return True, "Valid"

def shortest_path_bfs(grid, start, end):
    valid, message = validate_grid(grid, start, end)
    if not valid:
        return message
    rows = len(grid)
    cols = len(grid[0])
    queue = collections.deque([(start, [start])])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    return "No path found"

class PathFinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end

    def find(self):
        result = shortest_path_bfs(self.grid, self.start, self.end)
        return result

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    sample_start = (0, 0)
    sample_end = (4, 4)
    finder = PathFinder(sample_grid, sample_start, sample_end)
    print(finder.find())