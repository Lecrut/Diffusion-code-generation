import heapq

class AStarGrid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set()
        for obs in obstacles:
            self.obstacles.add(obs)

    def heuristic(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def is_valid(self, pos):
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            if pos not in self.obstacles:
                return True
        return False

    def get_neighbors(self, pos):
        x, y = pos
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.is_valid((nx, ny)):
                neighbors.append((nx, ny))
        return neighbors

    def find_path(self, start, end):
        if start == end:
            return [start]
        
        open_set = []
        heapq.heappush(open_set, (self.heuristic(start, end), 0, start))
        
        came_from = {}
        g_score = {start: 0}
        
        closed_set = set()
        
        while open_set:
            _, current_g, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]
            
            if current in closed_set:
                continue
            closed_set.add(current)
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
        
        return []

def run_example():
    width = 10
    height = 10
    obstacles = [(2, 2), (2, 3), (2, 4), (5, 5), (5, 6), (5, 7)]
    start = (0, 0)
    end = (9, 9)
    
    grid = AStarGrid(width, height, obstacles)
    path = grid.find_path(start, end)
    print(path)

if __name__ == '__main__':
    run_example()