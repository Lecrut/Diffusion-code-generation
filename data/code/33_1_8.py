import heapq

class GridShortestPath:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shortest_path(self, start, end):
        if not self.grid or not self.grid[0]:
            return None, float('inf')

        start_row, start_col = start
        end_row, end_col = end

        if (start_row < 0 or start_row >= self.rows or
                start_col < 0 or start_col >= self.cols or
                end_row < 0 or end_row >= self.rows or
                end_col < 0 or end_col >= self.cols):
            return None, float('inf')

        if self.grid[start_row][start_col] == 1 or self.grid[end_row][end_col] == 1:
            return None, float('inf')

        distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        distances[start_row][start_col] = 0
        previous = [[None] * self.cols for _ in range(self.rows)]

        pq = [(0, start_row, start_col)]
        visited = set()

        while pq:
            current_dist, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == end_row and c == end_col:
                break

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < self.rows and
                        0 <= nc < self.cols and
                        (nr, nc) not in visited and
                        self.grid[nr][nc] == 0):
                    new_dist = current_dist + 1
                    if new_dist < distances[nr][nc]:
                        distances[nr][nc] = new_dist
                        previous[nr][nc] = (r, c)
                        heapq.heappush(pq, (new_dist, nr, nc))

        if distances[end_row][end_col] == float('inf'):
            return None, float('inf')

        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = previous[curr[0]][curr[1]]
        path.reverse()

        return path, distances[end_row][end_col]

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    solver = GridShortestPath(grid)
    start_pos = (0, 0)
    end_pos = (4, 4)

    path, distance = solver.shortest_path(start_pos, end_pos)
    print(path)
    print(distance)