import heapq

def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None, None

    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    closed_set = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(current)
            path.reverse()
            return path, g_score[end]

        if current in closed_set:
            continue
        closed_set.add(current)

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                if neighbor in closed_set:
                    continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, end)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))

    return None, None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    
    path, cost = astar(grid, start_node, end_node)
    print(f"Path: {path}, Cost: {cost}")