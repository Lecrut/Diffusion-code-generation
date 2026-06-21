import heapq

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self, start, end):
        if not self.grid or not self.grid[0]:
            return []
        if self.grid[start[0]][start[1]] == 1 or self.grid[end[0]][end[1]] == 1:
            return []
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from = {}
        g_score = {start: 0}
        
        open_set_hash = set()
        open_set_hash.add(start)
        
        while open_set:
            current = heapq.heappop(open_set)
            current_node = current[1]
            open_set_hash.discard(current_node)
            
            if current_node == end:
                path = []
                while current_node in came_from:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.append(start)
                return path[::-1]
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_row = current_node[0] + dr
                neighbor_col = current_node[1] + dc
                
                if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                    if self.grid[neighbor_row][neighbor_col] == 1:
                        continue
                    
                    neighbor = (neighbor_row, neighbor_col)
                    tentative_g = g_score[current_node] + 1
                    
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current_node
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self.heuristic(neighbor, end)
                        
                        if neighbor not in open_set_hash:
                            heapq.heappush(open_set, (f_score, neighbor))
                            open_set_hash.add(neighbor)
        return []

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    pathfinder = GridPathfinder(grid)
    start = (0, 0)
    end = (4, 4)
    
    result = pathfinder.find_path(start, end)
    print(result)
    
    blocked_grid = [
        [0, 1],
        [1, 0]
    ]
    
    pathfinder2 = GridPathfinder(blocked_grid)
    result2 = pathfinder2.find_path((0, 0), (1, 1))
    print(result2)