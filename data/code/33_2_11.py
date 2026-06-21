import heapq

class GridPathfinder:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def get_neighbors(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            n_row, n_col = row + dr, col + dc
            if self.is_valid(n_row, n_col):
                neighbors.append((n_row, n_col))
        return neighbors

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self):
        if not self.is_valid(self.start[0], self.start[1]) or not self.is_valid(self.end[0], self.end[1]):
            return None, None
        
        if self.start == self.end:
            return [self.start], 0

        open_set = []
        heapq.heappush(open_set, (0, self.start))
        
        came_from = {}
        g_score = {self.start: 0}
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current == self.end:
                path = []
                temp = current
                while temp in came_from:
                    path.append(temp)
                    temp = came_from[temp]
                path.append(self.start)
                path.reverse()
                return path, g_score[self.end]

            for neighbor in self.get_neighbors(current[0], current[1]):
                tentative_g = g_score[current] + 1
                
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, self.end)
                    heapq.heappush(open_set, (f_score, neighbor))
                    
        return None, None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    end = (4, 4)
    
    pathfinder = GridPathfinder(grid, start, end)
    path, cost = pathfinder.find_path()
    
    print(cost)
    print(path)