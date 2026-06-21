import heapq

def shortest_path(grid):
    if not grid or not grid[0]:
        return []
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return []
    pq = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    while pq:
        current_cost, current = heapq.heappop(pq)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        if current_cost > cost_so_far.get(current, float('inf')):
            continue
        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_cost = current_cost + 1
                if new_cost < cost_so_far.get((nr, nc), float('inf')):
                    cost_so_far[(nr, nc)] = new_cost
                    heapq.heappush(pq, (new_cost, (nr, nc)))
                    came_from[(nr, nc)] = current
    return []

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0]
    ]
    result = shortest_path(sample_grid)
    print(result)