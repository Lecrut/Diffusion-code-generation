import heapq

class DijkstraGrid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, row, col):
        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and self.grid[row][col] != float('inf')
        )

    def compute_shortest_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return float('inf'), []

        dist = [[float('inf')] * self.cols for _ in range(self.rows)]
        prev = [[None] * self.cols for _ in range(self.rows)]
        dist[start[0]][start[1]] = 0
        pq = [(0, start[0], start[1])]

        while pq:
            d, r, c = heapq.heappop(pq)
            if d > dist[r][c]:
                continue
            if (r, c) == end:
                path = []
                curr = end
                while curr is not None:
                    path.append(curr)
                    curr = prev[curr[0]][curr[1]]
                path.reverse()
                return d, path

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc):
                    new_dist = dist[r][c] + self.grid[nr][nc]
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        prev[nr][nc] = (r, c)
                        heapq.heappush(pq, (new_dist, nr, nc))

        return float('inf'), []

if __name__ == '__main__':
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    end = (2, 2)
    dijkstra = DijkstraGrid(grid)
    distance, path = dijkstra.compute_shortest_path(start, end)
    print(distance)
    print(path)

    empty_grid = []
    dijkstra_empty = DijkstraGrid(empty_grid)
    dist_empty, path_empty = dijkstra_empty.compute_shortest_path((0, 0), (0, 0))
    print(dist_empty)
    print(path_empty)

    blocked_grid = [
        [0, float('inf'), 2],
        [3, float('inf'), 5],
        [6, 7, 8]
    ]
    dijkstra_blocked = DijkstraGrid(blocked_grid)
    dist_blocked, path_blocked = dijkstra_blocked.compute_shortest_path((0, 0), (2, 2))
    print(dist_blocked)
    print(path_blocked)