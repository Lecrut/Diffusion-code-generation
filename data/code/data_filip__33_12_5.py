import heapq
from typing import List, Tuple, Optional

class GridPathfinder:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get_shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return None
        
        if self.grid[start[0]][start[1]] == 0:
            return None
        if self.grid[end[0]][end[1]] == 0:
            return None

        distances = {}
        previous = {}
        pq = []
        
        distances[start] = 0
        heapq.heappush(pq, (0, start))
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current == end:
                path = []
                while current is not None:
                    path.append(current)
                    current = previous.get(current)
                return path[::-1]
            
            if current_dist > distances.get(current, float('inf')):
                continue
            
            r, c = current
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                
                if self.is_valid(nr, nc) and self.grid[nr][nc] != 0:
                    weight = self.grid[nr][nc]
                    distance = current_dist + weight
                    
                    if distance < distances.get((nr, nc), float('inf')):
                        distances[(nr, nc)] = distance
                        previous[(nr, nc)] = current
                        heapq.heappush(pq, (distance, (nr, nc)))
        
        return None

if __name__ == '__main__':
    sample_grid = [
        [1, 2, 3, 0],
        [4, 0, 6, 1],
        [7, 8, 9, 1],
        [1, 2, 1, 1]
    ]
    start_node = (0, 0)
    end_node = (3, 3)
    pathfinder = GridPathfinder(sample_grid)
    result_path = pathfinder.get_shortest_path(start_node, end_node)
    print(result_path)