import heapq
from typing import List, Tuple, Optional

class GridPathfinder:
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != 1

    def find_shortest_path(self) -> Tuple[Optional[int], Optional[List[Tuple[int, int]]]]:
        if not self.is_valid(self.start[0], self.start[1]) or not self.is_valid(self.end[0], self.end[1]):
            return None, None
        
        distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        distances[self.start[0]][self.start[1]] = self.grid[self.start[0]][self.start[1]]
        parents = {}
        pq = [(self.grid[self.start[0]][self.start[1]], self.start)]
        
        while pq:
            current_dist, (r, c) = heapq.heappop(pq)
            
            if (r, c) == self.end:
                path = []
                curr = self.end
                while curr != self.start:
                    path.append(curr)
                    curr = parents[curr]
                path.append(self.start)
                path.reverse()
                return current_dist, path
            
            if current_dist > distances[r][c]:
                continue
            
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc):
                    new_dist = current_dist + self.grid[nr][nc]
                    if new_dist < distances[nr][nc]:
                        distances[nr][nc] = new_dist
                        parents[(nr, nc)] = (r, c)
                        heapq.heappush(pq, (new_dist, (nr, nc)))
        
        return None, None

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    pathfinder = GridPathfinder(sample_grid, start_node, end_node)
    distance, path = pathfinder.find_shortest_path()
    print(f"Shortest Distance: {distance}")
    print(f"Path: {path}")