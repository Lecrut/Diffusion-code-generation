import collections

class GridPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def find_shortest_path(self, start, end):
        if start == end:
            return [start]
        
        q_start = collections.deque([start])
        q_end = collections.deque([end])
        visited_start = {start: [start]}
        visited_end = {end: [end]}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q_start and q_end:
            if len(q_start) <= len(q_end):
                curr = q_start.popleft()
                for dr, dc in directions:
                    nr, nc = curr[0] + dr, curr[1] + dc
                    if self.is_valid(nr, nc):
                        neighbor = (nr, nc)
                        if neighbor in visited_start:
                            continue
                        visited_start[neighbor] = visited_start[curr] + [neighbor]
                        if neighbor in visited_end:
                            return visited_start[neighbor][:-1] + visited_end[neighbor][::-1]
                        q_start.append(neighbor)
            else:
                curr = q_end.popleft()
                for dr, dc in directions:
                    nr, nc = curr[0] + dr, curr[1] + dc
                    if self.is_valid(nr, nc):
                        neighbor = (nr, nc)
                        if neighbor in visited_end:
                            continue
                        visited_end[neighbor] = visited_end[curr] + [neighbor]
                        if neighbor in visited_start:
                            return visited_start[neighbor][:-1] + visited_end[neighbor][::-1]
                        q_end.append(neighbor)
        return None

if __name__ == '__main__':
    grid_data = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    finder = GridPathfinder(grid_data)
    result = finder.find_shortest_path(start_node, end_node)
    print(result)