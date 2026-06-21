import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None
    if start == goal:
        return [start]
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {}
    g_score[start] = 0
    f_score = {}
    f_score[start] = heuristic(start, goal)
    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        if current in f_score and current_f > f_score[current]:
            continue
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            nr, nc = neighbor
            if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 0):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None
if __name__ == '__main__':
    grid_map = [[0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]
    start_point = (0, 0)
    end_point = (4, 4)
    result_path = a_star(grid_map, start_point, end_point)
    print(result_path)