from collections import deque

class ShortestPathBinaryMatrix:
    def shortestPathBinaryMatrix(self, grid):
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 1 and cols == 1:
            return 1
        
        queue = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        if nr == rows - 1 and nc == cols - 1:
                            return dist + 1
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))
        
        return -1

if __name__ == '__main__':
    solver = ShortestPathBinaryMatrix()
    sample_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = solver.shortestPathBinaryMatrix(sample_grid)
    print(result)