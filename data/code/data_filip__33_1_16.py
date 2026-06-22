import heapq

class GridGraph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_neighbors(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] != 1:
                neighbors.append((new_row, new_col))
        return neighbors

    def dijkstra(self, start, end):
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols) or self.grid[start[0]][start[1]] == 1:
            return None
        if not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols) or self.grid[end[0]][end[1]] == 1:
            return None

        distances = {}
        previous = {}
        priority_queue = []

        for r in range(self.rows):
            for c in range(self.cols):
                distances[(r, c)] = float('inf')
                previous[(r, c)] = None
        
        distances[start] = 0
        heapq.heappush(priority_queue, (0, start))

        while priority_queue:
            current_dist, (current_r, current_c) = heapq.heappop(priority_queue)

            if (current_r, current_c) == end:
                break

            if current_dist > distances[(current_r, current_c)]:
                continue

            for neighbor_r, neighbor_c in self.get_neighbors(current_r, current_c):
                weight = 1
                if self.grid[neighbor_r][neighbor_c] == 2:
                    weight = 2
                distance = current_dist + weight

                if distance < distances[(neighbor_r, neighbor_c)]:
                    distances[(neighbor_r, neighbor_c)] = distance
                    previous[(neighbor_r, neighbor_c)] = (current_r, current_c)
                    heapq.heappush(priority_queue, (distance, (neighbor_r, neighbor_c)))

        if distances[end] == float('inf'):
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
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 2, 2, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    graph = GridGraph(sample_grid)
    result_path = graph.dijkstra(start_node, end_node)
    print(result_path)