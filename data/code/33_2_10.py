class GridPathfinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.visited = set()
        self.parent = {}

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0 and (r, c) not in self.visited

    def manhattan_distance(self, r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)

    def a_star(self):
        open_set = []
        closed_set = set()
        g_score = {self.start: 0}
        f_score = {self.start: self.manhattan_distance(*self.start, *self.end)}
        open_set.append((f_score[self.start], self.start))

        while open_set:
            current_f, current = open_set.pop(0)
            
            if current == self.end:
                return self._reconstruct_path(current)

            if current in closed_set:
                continue
            closed_set.add(current)

            r, c = current
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (r + dr, c + dc)
                
                if neighbor in closed_set:
                    continue
                nr, nc = neighbor
                if not self.is_valid(nr, nc):
                    continue
                
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    self.parent[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.manhattan_distance(*neighbor, *self.end)
                    f_score[neighbor] = f
                    open_set.append((f, neighbor))
            
            open_set.sort(key=lambda x: x[0])
        
        return None

    def _reconstruct_path(self, current):
        path = [current]
        while current in self.parent:
            current = self.parent[current]
            path.append(current)
        return list(reversed(path))

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    pathfinder = GridPathfinder(grid, start, end)
    path = pathfinder.a_star()
    print(path)