import heapq

def astar_shortest_path(grid, start, goal):
    if not grid or not grid[0]:
        return None
    rows = len(grid)
    cols = len(grid[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
        return None
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d_row, d_col in directions:
            neighbor_row = current[0] + d_row
            neighbor_col = current[1] + d_col
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                if grid[neighbor_row][neighbor_col] == 1:
                    continue
                neighbor = (neighbor_row, neighbor_col)
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    goal_point = (4, 4)
    result = astar_shortest_path(sample_grid, start_point, goal_point)
    print(result)