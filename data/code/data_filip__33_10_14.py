import heapq

def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), start))
    came_from = {}
    g_score = {start: 0}
    closed_set = set()
    while open_set:
        current_g, current = heapq.heappop(open_set)
        if current in closed_set:
            if current_g > g_score[current]:
                continue
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        closed_set.add(current)
        current_row, current_col = current
        neighbors = [(current_row - 1, current_col), (current_row + 1, current_col), (current_row, current_col - 1), (current_row, current_col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if not (0 <= n_row < rows and 0 <= n_col < cols):
                continue
            if grid[n_row][n_col] == 1:
                continue
            if neighbor in closed_set:
                continue
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))
    return []
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    start_node = (0, 0)
    end_node = (4, 4)
    path = astar(grid, start_node, end_node)
    print(path)