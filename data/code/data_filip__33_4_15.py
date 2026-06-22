from collections import deque

class BidirectionalBFS:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def get_neighbors(self, r, c):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def reconstruct_path(self, came_from, start, end, is_forward):
        path = [end]
        current = end
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        if not is_forward:
            path.reverse()
        return path

    def find_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return None
        if start == end:
            return [start]

        front_visited = {start: None}
        back_visited = {end: None}
        front_queue = deque([start])
        back_queue = deque([end])
        meeting_point = None

        while front_queue and back_queue:
            if len(front_queue) <= len(back_queue):
                current = front_queue.popleft()
                for neighbor in self.get_neighbors(*current):
                    if neighbor in front_visited:
                        continue
                    front_visited[neighbor] = current
                    if neighbor in back_visited:
                        meeting_point = neighbor
                        break
                    front_queue.append(neighbor)
                if meeting_point:
                    break
            else:
                current = back_queue.popleft()
                for neighbor in self.get_neighbors(*current):
                    if neighbor in back_visited:
                        continue
                    back_visited[neighbor] = current
                    if neighbor in front_visited:
                        meeting_point = neighbor
                        break
                    back_queue.append(neighbor)
                if meeting_point:
                    break

        if meeting_point is None:
            return None

        path_start = self.reconstruct_path(front_visited, start, meeting_point, True)
        path_end = self.reconstruct_path(back_visited, meeting_point, end, False)
        if path_start:
            path_start.pop()
        return path_start + path_end

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    solver = BidirectionalBFS(grid)
    result = solver.find_path(start_node, end_node)
    print(result)