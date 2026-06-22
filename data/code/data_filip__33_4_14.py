from collections import deque

class GridPathFinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def find_shortest_path(self, start, end):
        if not self.is_valid(start[0], start[1]) or not self.is_valid(end[0], end[1]):
            return None
        if start == end:
            return [start]

        start_queue = deque([start])
        end_queue = deque([end])
        start_visited = {start: start}
        end_visited = {end: end}
        start_path = {start: []}
        end_path = {end: []}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while start_queue and end_queue:
            if len(start_queue) <= len(end_queue):
                meeting_node = self._bfs_step(start_queue, start_visited, end_visited, start_path, end_path, directions)
                if meeting_node:
                    return self._reconstruct_path(start_path, end_path, meeting_node)
            else:
                meeting_node = self._bfs_step(end_queue, end_visited, start_visited, end_path, start_path, directions)
                if meeting_node:
                    return self._reconstruct_path(end_path, start_path, meeting_node)
        return None

    def _bfs_step(self, queue, visited, other_visited, path_map, other_path_map, directions):
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc) and (nr, nc) not in visited:
                visited[(nr, nc)] = (r, c)
                path_map[(nr, nc)] = path_map[(r, c)] + [(nr, nc)]
                queue.append((nr, nc))
                if (nr, nc) in other_visited:
                    return (nr, nc)
        return None

    def _reconstruct_path(self, forward_map, backward_map, meeting_node):
        forward_path = forward_map[meeting_node]
        backward_node = meeting_node
        backward_stack = []
        while backward_node in backward_map and backward_map[backward_node] is not None:
            prev = backward_map[backward_node]
            if prev is not backward_node:
                backward_stack.append(prev)
                backward_node = prev
            else:
                break
        if not backward_stack:
            return forward_path
        return forward_path + list(reversed(backward_stack))

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    finder = GridPathFinder(sample_grid)
    result = finder.find_shortest_path(start_point, end_point)
    print(result)