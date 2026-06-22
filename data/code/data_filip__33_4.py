from collections import deque

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def find_shortest_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return []
        
        if start == end:
            return [start]

        forward_queue = deque([start])
        backward_queue = deque([end])
        forward_visited = {start: None}
        backward_visited = {end: None}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        meeting_point = None

        while forward_queue and backward_queue:
            if len(forward_queue) <= len(backward_queue):
                current = forward_queue.popleft()
                for dr, dc in directions:
                    nr, nc = current[0] + dr, current[1] + dc
                    if self.is_valid(nr, nc) and (nr, nc) not in forward_visited:
                        forward_visited[(nr, nc)] = current
                        forward_queue.append((nr, nc))
                        if (nr, nc) in backward_visited:
                            meeting_point = (nr, nc)
                            break
                if meeting_point:
                    break
            else:
                current = backward_queue.popleft()
                for dr, dc in directions:
                    nr, nc = current[0] + dr, current[1] + dc
                    if self.is_valid(nr, nc) and (nr, nc) not in backward_visited:
                        backward_visited[(nr, nc)] = current
                        backward_queue.append((nr, nc))
                        if (nr, nc) in forward_visited:
                            meeting_point = (nr, nc)
                            break
                if meeting_point:
                    break

        if meeting_point is None:
            return []

        path = []
        node = meeting_point
        while node is not None:
            path.append(node)
            node = forward_visited[node]
        path.reverse()

        node = backward_visited[meeting_point]
        while node is not None:
            path.append(node)
            node = backward_visited[node]

        return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    pathfinder = GridPathfinder(grid)
    result_path = pathfinder.find_shortest_path(start_point, end_point)
    print(result_path)