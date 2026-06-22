import heapq

def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def heuristic(pos):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        if current in closed_set:
            continue
        closed_set.add(current)

        row, col = current
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for next_pos in neighbors:
            nr, nc = next_pos
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1:
                continue

            neighbor = (nr, nc)
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor)
                f_score[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))

    return []

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_node = (0, 0)
    end_node = (4, 4)
    result = astar(grid, start_node, end_node)
    print(result)