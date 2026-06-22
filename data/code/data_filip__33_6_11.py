from collections import deque

class GridShortestPath:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def find_path(self, start, end):
        if not self.rows or not self.cols:
            return None
        sr, sc = start
        er, ec = end
        if sr < 0 or sr >= self.rows or sc < 0 or sc >= self.cols:
            return None
        if er < 0 or er >= self.rows or ec < 0 or ec >= self.cols:
            return None
        if self.grid[sr][sc] == 1 or self.grid[er][ec] == 1:
            return None
        queue = deque([(sr, sc, [(sr, sc)])])
        visited = set()
        visited.add((sr, sc))
        while queue:
            r, c, path = queue.popleft()
            if r == er and c == ec:
                return path
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if (nr, nc) not in visited and self.grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        new_path = list(path)
                        new_path.append((nr, nc))
                        queue.append((nr, nc, new_path))
        return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    solver = GridShortestPath(sample_grid)
    start_pos = (0, 0)
    end_pos = (4, 4)
    result_path = solver.find_path(start_pos, end_pos)
    print(result_path)