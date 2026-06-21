from collections import deque

def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    if start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols:
        return -1
    if end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols:
        return -1
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1
    if start == end:
        return 0
    queue = deque([start])
    visited = {start}
    steps = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        steps += 1
        level_size = len(queue)
        for _ in range(level_size):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                    if (nr, nc) == end:
                        return steps
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    start_node = (0, 0)
    end_node = (2, 2)
    result = shortest_path(grid, start_node, end_node)
    print(result)
    grid_blocked = [
        [0, 1],
        [1, 0]
    ]
    start_node_blocked = (0, 0)
    end_node_blocked = (1, 1)
    result_blocked = shortest_path(grid_blocked, start_node_blocked, end_node_blocked)
    print(result_blocked)