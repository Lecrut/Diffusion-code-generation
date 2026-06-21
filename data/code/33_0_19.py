from collections import deque

def find_shortest_path(grid):
    if not grid or not grid[0]:
        return None

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
        return None

    visited = set()
    queue = deque()
    queue.append((start, []))
    visited.add(start)

    while queue:
        (current_r, current_c), path = queue.popleft()
        current_path = path + [(current_r, current_c)]

        if (current_r, current_c) == end:
            return current_path

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_r = current_r + dr
            new_c = current_c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != 'X' and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append(((new_r, new_c), current_path))

    return None

if __name__ == '__main__':
    sample_grid = [
        ['S', '.', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', 'X', '.'],
        ['X', 'X', '.', '.', '.'],
        ['.', '.', '.', 'X', 'E']
    ]
    result = find_shortest_path(sample_grid)
    print(result)