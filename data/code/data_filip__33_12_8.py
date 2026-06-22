import heapq
from typing import List, Tuple, Optional

Direction = Tuple[int, int]
UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)
DIRECTIONS: List[Direction] = [UP, DOWN, LEFT, RIGHT]

class GridGraph:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, row: int, col: int) -> List[Tuple[int, int, int]]:
        neighbors = []
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                weight = self.grid[nr][nc]
                neighbors.append((nr, nc, weight))
        return neighbors

    def find_shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[Tuple[List[Tuple[int, int]], int]]:
        if not self.grid or self.rows == 0 or self.cols == 0:
            return None
        start_row, start_col = start
        end_row, end_col = end
        if not (0 <= start_row < self.rows and 0 <= start_col < self.cols):
            return None
        if not (0 <= end_row < self.rows and 0 <= end_col < self.cols):
            return None
        if self.grid[start_row][start_col] == 0:
            return None
        distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        distances[start_row][start_col] = self.grid[start_row][start_col]
        predecessors = [[None] * self.cols for _ in range(self.rows)]
        heap = [(distances[start_row][start_col], start_row, start_col)]
        visited = set()
        while heap:
            current_dist, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == end_row and c == end_col:
                break
            for nr, nc, weight in self.get_neighbors(r, c):
                if (nr, nc) not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distances[nr][nc]:
                        distances[nr][nc] = new_dist
                        predecessors[nr][nc] = (r, c)
                        heapq.heappush(heap, (new_dist, nr, nc))
        if distances[end_row][end_col] == float('inf'):
            return None
        path = []
        current = (end_row, end_col)
        while current is not None:
            path.append(current)
            current = predecessors[current[0]][current[1]]
        path.reverse()
        return path, distances[end_row][end_col]

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    graph = GridGraph(sample_grid)
    start_node = (0, 0)
    end_node = (2, 2)
    result = graph.find_shortest_path(start_node, end_node)
    if result is None:
        print("No path found")
    else:
        path, total_cost = result
        print(f"Path: {path}")
        print(f"Total Cost: {total_cost}")