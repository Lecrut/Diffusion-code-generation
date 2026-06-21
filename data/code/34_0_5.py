import heapq

def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    if start == end:
        return [start]
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    closed_set = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == end:
            return reconstruct_path(came_from, current)
        if current in closed_set:
            continue
        closed_set.add(current)
        cr, cc = current
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if neighbor in closed_set:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, end)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    path = astar(grid, start, end)
    print(path)