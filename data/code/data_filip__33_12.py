import heapq
import sys

class GridGraph:
    def __init__(self, grid):
        if not grid or not grid[0]:
            self.rows = 0
            self.cols = 0
            self.grid = []
            return
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

    def get_neighbors(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != -1:
                    neighbors.append((nr, nc, self.grid[nr][nc]))
        return neighbors

    def dijkstra(self, start, end):
        if not self.rows or not self.cols:
            return None
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols):
            return None
        if not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols):
            return None
        if self.grid[start[0]][start[1]] == -1 or self.grid[end[0]][end[1]] == -1:
            return None

        distances = {}
        previous = {}
        pq = []
        heapq.heappush(pq, (0, start))
        distances[start] = 0
        previous[start] = None

        while pq:
            current_dist, current = heapq.heappop(pq)
            if current == end:
                break
            if current_dist > distances.get(current, float('inf')):
                continue
            for nr, nc, weight in self.get_neighbors(current[0], current[1]):
                neighbor = (nr, nc)
                new_dist = current_dist + weight
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))

        if end not in distances:
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path, distances[end]

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 4, 3],
        [2, 1, 99, 2],
        [3, 4, 1, 0]
    ]
    graph = GridGraph(sample_grid)
    start_point = (0, 0)
    end_point = (2, 3)
    result = graph.dijkstra(start_point, end_point)
    if result:
        path, total_cost = result
        print(f"Path: {path}, Total Cost: {total_cost}")
    else:
        print("No path found")