import heapq
import sys

class GridGraph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, node):
        r, c = node
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                weight = self.grid[nr][nc]
                if weight >= 0:
                    neighbors.append(((nr, nc), weight))
        return neighbors

    def dijkstra(self, start, end):
        if not self.grid or not self.grid[0]:
            return None, []
        
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols):
            return None, []
        
        if not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols):
            return None, []
        
        if self.grid[start[0]][start[1]] < 0 or self.grid[end[0]][end[1]] < 0:
            return None, []

        distances = {}
        previous = {}
        queue = []

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] >= 0:
                    distances[(r, c)] = float('inf')
                    previous[(r, c)] = None

        distances[start] = 0
        heapq.heappush(queue, (0, start))

        while queue:
            current_dist, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.get_neighbors(current_node):
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (new_dist, neighbor))

        if distances[end] == float('inf'):
            return None, []

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return distances[end], path

def main():
    sample_grid = [
        [0, 3, 2, float('inf')],
        [1, float('inf'), 4, 1],
        [2, 1, 1, 2],
        [1, 1, 0, 1]
    ]
    
    start_node = (0, 0)
    end_node = (3, 3)
    
    graph = GridGraph(sample_grid)
    distance, path = graph.dijkstra(start_node, end_node)
    
    print(f"Shortest distance: {distance}")
    print(f"Path: {path}")

if __name__ == '__main__':
    main()