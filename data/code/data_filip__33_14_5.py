import heapq
import math
from typing import List, Tuple, Dict, Optional, Set

class GridPathfinder:
    def __init__(self, grid: List[List[float]], diagonal_cost: float = 1.414, cardinal_cost: float = 1.0):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_cost = diagonal_cost
        self.cardinal_cost = cardinal_cost

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        r, c = pos
        neighbors = []
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                cost = self.diagonal_cost if abs(dr) == 1 and abs(dc) == 1 else self.cardinal_cost
                neighbors.append(((nr, nc), cost))
        return neighbors

    def _heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        r1, c1 = pos
        r2, c2 = goal
        dr = abs(r1 - r2)
        dc = abs(c1 - c2)
        return self.cardinal_cost * (dr + dc) + (self.diagonal_cost - 2 * self.cardinal_cost) * min(dr, dc)

    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if self.grid[start[0]][start[1]] == float('inf') or self.grid[goal[0]][goal[1]] == float('inf'):
            return None
        if start == goal:
            return [start]
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}
        g_score: Dict[Tuple[int, int], float] = {start: 0}
        closed_set: Set[Tuple[int, int]] = set()
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current in closed_set:
                continue
            closed_set.add(current)
            
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from.get(current)
                return path[::-1]
            
            for neighbor, move_cost in self._get_neighbors(current):
                if self.grid[neighbor[0]][neighbor[1]] == float('inf'):
                    continue
                    
                tentative_g = g_score[current] + move_cost
                
                if neighbor in closed_set:
                    continue
                    
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))
        
        return None

if __name__ == '__main__':
    grid_map = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    pathfinder = GridPathfinder(grid_map)
    start_node = (0, 0)
    end_node = (4, 4)
    
    result_path = pathfinder.find_path(start_node, end_node)
    print(result_path)