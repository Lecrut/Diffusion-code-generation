import heapq

class AStar:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self.directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

    def is_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def heuristic(self, r1, c1, r2, c2):
        return max(abs(r1 - r2), abs(c1 - c2))

    def get_neighbors(self, r, c):
        neighbors = []
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def find_path(self):
        if not self.is_valid(self.start[0], self.start[1]) or not self.is_valid(self.end[0], self.end[1]):
            return [], float('inf')
        
        if self.start == self.end:
            return [self.start], 0

        open_set = []
        heapq.heappush(open_set, (0, self.start))
        
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(*self.start, *self.end)}
        
        came_from = {}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == self.end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path, g_score[self.end]

            for nr, nc in self.get_neighbors(current[0], current[1]):
                neighbor = (nr, nc)
                
                if current == self.start:
                    cost = self.heuristic(current[0], current[1], nr, nc)
                else:
                    dist = 1 if abs(current[0] - nr) + abs(current[1] - nc) == 1 else 1.414
                    cost = dist
                
                tentative_g = g_score[current] + cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(nr, nc, *self.end)
                    f_score[neighbor] = f
                    
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f, neighbor))
        
        return [], float('inf')

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    
    astar = AStar(grid, start, end)
    path, cost = astar.find_path()
    
    print(f"Path: {path}")
    print(f"Cost: {cost}")

if __name__ == '__main__':
    main()