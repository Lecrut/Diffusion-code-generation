class BinaryGridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        if not grid or not grid[0]:
            self.rows = 0
            self.cols = 0
        else:
            self.rows = len(grid)
            self.cols = len(grid[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def find_shortest_path(self, start, end):
        if self.rows == 0 or self.cols == 0:
            return []
        if self.grid[start[0]][start[1]] == 1 or self.grid[end[0]][end[1]] == 1:
            return []
        if start == end:
            return [start]
        
        queue = []
        queue.append((start[0], start[1], [start]))
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        visited[start[0]][start[1]] = True
        
        while queue:
            r, c, path = queue.pop(0)
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if not visited[nr][nc] and self.grid[nr][nc] == 0:
                        new_path = path + [(nr, nc)]
                        
                        if (nr, nc) == end:
                            return new_path
                        
                        visited[nr][nc] = True
                        queue.append((nr, nc, new_path))
        
        return []

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0]
    ]
    start_coords = (0, 0)
    end_coords = (3, 3)
    pathfinder = BinaryGridPathfinder(sample_grid)
    result_path = pathfinder.find_shortest_path(start_coords, end_coords)
    print(result_path)