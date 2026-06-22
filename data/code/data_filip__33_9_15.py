import heapq

class AStarGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def is_valid(self, row, col):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return False
        return self.grid[row][col] == 0

    def get_neighbors(self, row, col):
        moves = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]
        neighbors = []
        for dr, dc in moves:
            nr, nc = row + dr, col + dc
            if self.is_valid(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def heuristic(self, r1, c1, r2, c2):
        dist = max(abs(r1 - r2), abs(c1 - c2))
        return dist

    def find_path(self, start, end):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start[0], start[1], end[0], end[1])}
        
        while open_set:
            current = heapq.heappop(open_set)[1]
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]
            
            for neighbor in self.get_neighbors(current[0], current[1]):
                tentative_g = g_score[current] + (1.414 if abs(current[0] - neighbor[0]) + abs(current[1] - neighbor[1]) == 2 else 1)
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor[0], neighbor[1], end[0], end[1])
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

if __name__ == '__main__':
    grid = AStarGrid(10, 10)
    grid.grid[2][2] = 1
    grid.grid[2][3] = 1
    grid.grid[2][4] = 1
    grid.grid[3][2] = 1
    grid.grid[4][2] = 1
    grid.grid[5][5] = 1
    grid.grid[5][6] = 1
    grid.grid[5][7] = 1
    
    start_node = (0, 0)
    end_node = (9, 9)
    
    path = grid.find_path(start_node, end_node)
    print(path)