import heapq

def find_shortest_path(grid):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    if start is None or end is None:
        return []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def heuristic(node):
        r, c = node
        er, ec = end
        return abs(r - er) + abs(c - ec)
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        cr, cc = current
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '#':
                    continue
                tentative_g = g_score[current] + 1
                if (nr, nc) not in g_score or tentative_g < g_score[(nr, nc)]:
                    g_score[(nr, nc)] = tentative_g
                    f_score = tentative_g + heuristic((nr, nc))
                    heapq.heappush(open_set, (f_score, tentative_g, (nr, nc)))
                    came_from[(nr, nc)] = current
    return []

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '#', '.', '#', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['#', '#', '.', '#', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '#', '.', '#', 'E', '.'],
    ]
    result = find_shortest_path(sample_grid)
    print(result)