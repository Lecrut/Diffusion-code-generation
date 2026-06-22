import collections
import heapq

def shortest_path_grid(grid):
    if not grid or not grid[0]:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1
    if start == end:
        return 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add(start)
    queue = collections.deque()
    queue.append((start, 0))
    while queue:
        (r, c), dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                if (nr, nc) == end:
                    return dist + 1
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 0]
    ]
    result = shortest_path_grid(grid)
    print(result)