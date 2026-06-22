import collections

class GridPathfinder:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def _in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _is_walkable(self, r, c):
        return self.grid[r][c] == 0

    def _get_neighbors(self, r, c):
        neighbors = []
        for dr, dc in self.DIRECTIONS:
            nr, nc = r + dr, c + dc
            if self._in_bounds(nr, nc) and self._is_walkable(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def find_shortest_path(self, start, end):
        if not self._in_bounds(start[0], start[1]) or not self._in_bounds(end[0], end[1]):
            return []
        if not self._is_walkable(start[0], start[1]) or not self._is_walkable(end[0], end[1]):
            return []
        if start == end:
            return [start]

        forward_queue = collections.deque([start])
        backward_queue = collections.deque([end])
        forward_parents = {start: None}
        backward_parents = {end: None}
        forward_visited = {start}
        backward_visited = {end}

        meeting_point = None

        while forward_queue and backward_queue:
            if len(forward_queue) <= len(backward_queue):
                current = forward_queue.popleft()
                for neighbor in self._get_neighbors(current[0], current[1]):
                    if neighbor in backward_visited:
                        meeting_point = neighbor
                        forward_parents[neighbor] = current
                        break
                    if neighbor not in forward_visited:
                        forward_visited.add(neighbor)
                        forward_parents[neighbor] = current
                        forward_queue.append(neighbor)
                if meeting_point:
                    break
            else:
                current = backward_queue.popleft()
                for neighbor in self._get_neighbors(current[0], current[1]):
                    if neighbor in forward_visited:
                        meeting_point = neighbor
                        backward_parents[neighbor] = current
                        break
                    if neighbor not in backward_visited:
                        backward_visited.add(neighbor)
                        backward_parents[neighbor] = current
                        backward_queue.append(neighbor)
                if meeting_point:
                    break

        if meeting_point is None:
            return []

        path = []
        node = meeting_point
        while node is not None:
            path.append(node)
            node = forward_parents.get(node)
        path.reverse()
        
        node = backward_parents.get(meeting_point)
        while node is not None:
            path.append(node)
            node = backward_parents.get(node)
            
        return path

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    finder = GridPathfinder(sample_grid)
    result_path = finder.find_shortest_path(start_node, end_node)
    print(result_path)