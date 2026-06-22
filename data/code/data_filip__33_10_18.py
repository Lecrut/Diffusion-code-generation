import heapq

def a_star(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        if current_f > f_score.get(current, float('inf')):
            continue
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            nr, nc = neighbor
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1:
                continue
            if dr != 0 and dc != 0:
                step_cost = 1.414
            else:
                step_cost = 1.0
            tentative_g = g_score[current] + step_cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return []
if __name__ == '__main__':
    grid_map = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    start_point = (0, 0)
    end_point = (4, 4)
    path = a_star(grid_map, start_point, end_point)
    print(path)