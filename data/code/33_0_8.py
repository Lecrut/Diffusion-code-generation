from collections import deque

def find_shortest_path_bfs(grid):
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    queue = deque([(start, [start])])
    visited = set([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == end:
            return path

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    new_path = list(path)
                    new_path.append((new_row, new_col))
                    queue.append(((new_row, new_col), new_path))

    return None

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    shortest_path = find_shortest_path_bfs(sample_grid)
    print(shortest_path)