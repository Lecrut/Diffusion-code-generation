import heapq

class GridPathfinder:
    def __init__(self, grid, diagonal_cost=1.0, orthogonal_cost=1.0):
        if not grid:
            raise ValueError("Grid cannot be empty")
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_cost = diagonal_cost
        self.orthogonal_cost = orthogonal_cost
        self.visited = set()

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != '#'

    def get_neighbors(self, r, c):
        moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        results = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                if abs(dr) + abs(dc) == 2:
                    cost = self.diagonal_cost
                    if not self.is_valid(r, c + dc) or not self.is_valid(r + dr, c):
                        continue
                else:
                    cost = self.orthogonal_cost
                results.append((nr, nc, cost))
        return results

    def heuristic(self, r1, c1, r2, c2):
        dr = abs(r1 - r2)
        dc = abs(c1 - c2)
        return min(dr, dc) * self.diagonal_cost + (max(dr, dc) - min(dr, dc)) * self.orthogonal_cost

    def find_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return None, float('inf')
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start[0], start[1], end[0], end[1])}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, g_score[end]
            
            if current in self.visited:
                continue
            self.visited.add(current)
            
            for nr, nc, cost in self.get_neighbors(current[0], current[1]):
                neighbor = (nr, nc)
                if neighbor in self.visited:
                    continue
                
                tentative_g = g_score[current] + cost
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(nr, nc, end[0], end[1])
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        
        return None, float('inf')

if __name__ == '__main__':
    grid = [
        ['.', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]
    
    pathfinder = GridPathfinder(grid)
    start = (0, 0)
    end = (4, 4)
    
    path, cost = pathfinder.find_path(start, end)
    
    print(f"Path: {path}")
    print(f"Cost: {cost}")