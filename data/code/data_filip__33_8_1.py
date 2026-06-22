from collections import deque

class GridPathfinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def validate(self):
        if self.rows == 0 or self.cols == 0:
            raise ValueError("Grid cannot be empty")
        sr, sc = self.start
        er, ec = self.end
        if not (0 <= sr < self.rows and 0 <= sc < self.cols):
            raise ValueError("Start point out of bounds")
        if not (0 <= er < self.rows and 0 <= ec < self.cols):
            raise ValueError("End point out of bounds")
        if self.grid[sr][sc] == 1:
            raise ValueError("Start point is blocked")
        if self.grid[er][ec] == 1:
            raise ValueError("End point is blocked")
        return True

    def solve(self):
        self.validate()
        sr, sc = self.start
        er, ec = self.end
        if (sr, sc) == (er, ec):
            return [ (sr, sc) ]
        queue = deque([(sr, sc, [(sr, sc)])])
        visited = set()
        visited.add((sr, sc))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, path = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if (nr, nc) not in visited and self.grid[nr][nc] == 0:
                        new_path = path + [(nr, nc)]
                        if nr == er and nc == ec:
                            return new_path
                        visited.add((nr, nc))
                        queue.append((nr, nc, new_path))
        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    pathfinder = GridPathfinder(sample_grid, start_point, end_point)
    result = pathfinder.solve()
    print(result)