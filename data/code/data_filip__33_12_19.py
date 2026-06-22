import heapq
from typing import List, Tuple, Optional

class GridGraph:
    def __init__(self, grid: List[List[int]], obstacles: List[Tuple[int, int]] = None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.obstacles = set(obstacles) if obstacles else set()

    def get_neighbors(self, row: int, col: int) -> List[Tuple[Tuple[int, int], int]]:
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if (new_row, new_col) not in self.obstacles:
                    weight = self.grid[new_row][new_col]
                    neighbors.append(((new_row, new_col), weight))
        return neighbors

    def dijkstra(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[Tuple[int, List[Tuple[int, int]]]]:
        if start[0] < 0 or start[0] >= self.rows or start[1] < 0 or start[1] >= self.cols:
            return None
        if end[0] < 0 or end[0] >= self.rows or end[1] < 0 or end[1] >= self.cols:
            return None
        if start in self.obstacles or end in self.obstacles:
            return None
        if start == end:
            return (0, [start])
        
        distances = {start: 0}
        predecessors = {}
        pq = [(0, start)]
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current == end:
                path = []
                while current != start:
                    path.append(current)
                    current = predecessors[current]
                path.append(start)
                path.reverse()
                return (distances[end], path)
            
            if current_dist > distances.get(current, float('inf')):
                continue
            
            for neighbor, weight in self.get_neighbors(current[0], current[1]):
                distance = current_dist + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    predecessors[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        return None

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1, 2],
        [1, 5, 1, 3],
        [2, 1, 1, 1],
        [3, 2, 2, 1]
    ]
    sample_obstacles = [(1, 1), (2, 2)]
    start_pos = (0, 0)
    end_pos = (3, 3)
    
    graph = GridGraph(sample_grid, sample_obstacles)
    result = graph.dijkstra(start_pos, end_pos)
    
    if result:
        total_cost, path = result
        print(f"Total Cost: {total_cost}")
        print(f"Path: {path}")
    else:
        print("No path found")