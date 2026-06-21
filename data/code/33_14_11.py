import heapq
from typing import List, Tuple, Optional

class GridPathfinder:
    def __init__(self, grid: List[List[float]], diagonal_cost: float = 1.4142135623730951):
        self.grid = grid
        self.diagonal_cost = diagonal_cost
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def _get_neighbors(self, r: int, c: int) -> List[Tuple[int, int, float]]:
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                cost = self.diagonal_cost if abs(dr) + abs(dc) == 2 else 1.0
                neighbors.append((nr, nc, cost))
        return neighbors

    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if not self.grid or self.grid[start[0]][start[1]] == 0 or self.grid[end[0]][end[1]] == 0:
            return None
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from = {}
        g_score = {start: 0}
        
        while open_set:
            current_g, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return list(reversed(path))
            
            if current_g > g_score.get(current, float('inf')):
                continue
            
            for nr, nc, step_cost in self._get_neighbors(current[0], current[1]):
                neighbor = (nr, nc)
                if self.grid[nr][nc] == 0:
                    continue
                
                tentative_g = g_score[current] + step_cost
                
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    h = abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                    f = tentative_g + h
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

if __name__ == '__main__':
    grid_map = [
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.0, 1.0, 0.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 0.0, 0.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0]
    ]
    
    pathfinder = GridPathfinder(grid_map)
    start_node = (0, 0)
    end_node = (4, 4)
    
    result = pathfinder.find_path(start_node, end_node)
    print(result)