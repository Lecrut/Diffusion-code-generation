import heapq
from typing import List, Tuple, Optional, Dict

class GridGraph:
    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.rows = len(grid)
        if self.rows == 0:
            self.cols = 0
        else:
            self.cols = len(grid[0])

    def get_neighbors(self, row: int, col: int) -> List[Tuple[int, int]]:
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != -1:
                    neighbors.append((nr, nc))
        return neighbors

    def shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if self.rows == 0 or self.cols == 0:
            return None
        sr, sc = start
        er, ec = end
        if not (0 <= sr < self.rows and 0 <= sc < self.cols):
            return None
        if not (0 <= er < self.rows and 0 <= ec < self.cols):
            return None
        if self.grid[sr][sc] == -1 or self.grid[er][ec] == -1:
            return None

        distances: Dict[Tuple[int, int], int] = {start: self.grid[sr][sc]}
        previous: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
        heap: List[Tuple[int, Tuple[int, int]]] = [(self.grid[sr][sc], start)]
        visited: set = set()

        while heap:
            current_dist, (curr_r, curr_c) = heapq.heappop(heap)
            if (curr_r, curr_c) in visited:
                continue
            visited.add((curr_r, curr_c))

            if (curr_r, curr_c) == end:
                break

            for nr, nc in self.get_neighbors(curr_r, curr_c):
                if (nr, nc) in visited:
                    continue
                weight = self.grid[nr][nc]
                new_dist = current_dist + weight
                if (nr, nc) not in distances or new_dist < distances[nr]:
                    distances[(nr, nc)] = new_dist
                    previous[(nr, nc)] = (curr_r, curr_c)
                    heapq.heappush(heap, (new_dist, (nr, nc)))

        if end not in distances:
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 2, -1],
        [4, 1, 2, 5],
        [2, 3, 1, 2],
        [5, 1, 3, 4]
    ]
    grid_graph = GridGraph(sample_grid)
    start_node = (0, 0)
    end_node = (3, 3)
    result_path = grid_graph.shortest_path(start_node, end_node)
    print(result_path)