import heapq
from typing import List, Tuple, Optional, Set, Dict

class GridPathfinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end

    def _heuristic(self, pos: Tuple[int, int]) -> int:
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        r, c = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    neighbors.append((nr, nc))
        return neighbors

    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        if self.grid[self.start[0]][self.start[1]] != 0 or self.grid[self.end[0]][self.end[1]] != 0:
            return None
        
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        
        came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}
        
        g_score: Dict[Tuple[int, int], int] = {self.start: 0}
        
        f_score: Dict[Tuple[int, int], int] = {self.start: self._heuristic(self.start)}
        
        open_set_hash: Set[Tuple[int, int]] = {self.start}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current not in open_set_hash:
                continue
            
            open_set_hash.remove(current)
            
            if current == self.end:
                path = []
                while current in came_from and came_from[current] is not None:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path
            
            for neighbor in self._get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor)
                    
                    if neighbor not in f_score or f < f_score[neighbor]:
                        f_score[neighbor] = f
                        if neighbor not in open_set_hash:
                            heapq.heappush(open_set, (f, neighbor))
                            open_set_hash.add(neighbor)
        
        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    end = (4, 4)
    
    pathfinder = GridPathfinder(grid, start, end)
    result = pathfinder.find_path()
    
    print(result)