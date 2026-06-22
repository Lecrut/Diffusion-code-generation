import heapq

class AStarSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def heuristic(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny] == 0:
                    neighbors.append((nx, ny))
        return neighbors

    def find_shortest_path(self, start, end):
        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from = {}
        
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        
        open_set_hash = {start}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current not in open_set_hash:
                continue
            open_set_hash.discard(current)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, end)
                    f_score[neighbor] = f
                    
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f, neighbor))
                        open_set_hash.add(neighbor)
        
        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    end_pos = (4, 4)
    
    solver = AStarSearch(grid)
    path = solver.find_shortest_path(start_pos, end_pos)
    
    print(path)