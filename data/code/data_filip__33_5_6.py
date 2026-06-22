import heapq

def find_minimum_cost_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    priority_queue = [(grid[0][0], 0, 0)]
    while priority_queue:
        cost, r, c = heapq.heappop(priority_queue)
        if r == rows - 1 and c == cols - 1:
            return cost
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                new_cost = cost + grid[nr][nc]
                heapq.heappush(priority_queue, (new_cost, nr, nc))
    return -1

if __name__ == '__main__':
    sample_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = find_minimum_cost_path(sample_grid)
    print(result)