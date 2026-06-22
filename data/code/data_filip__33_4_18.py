import collections

def bidirectional_bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def get_neighbors(pos):
        r, c = pos
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                yield (nr, nc)

    if grid[start[0]][start[1]] != 0 or grid[end[0]][end[1]] != 0:
        return None

    if start == end:
        return [start]

    queue_start = collections.deque([start])
    visited_start = {start: None}

    queue_end = collections.deque([end])
    visited_end = {end: None}

    meeting_point = None

    while queue_start and queue_end:
        if len(queue_start) <= len(queue_end):
            current_queue, current_visited, other_visited = queue_start, visited_start, visited_end
        else:
            current_queue, current_visited, other_visited = queue_end, visited_end, visited_start

        level_size = len(current_queue)
        for _ in range(level_size):
            current = current_queue.popleft()
            for neighbor in get_neighbors(current):
                if neighbor not in current_visited:
                    current_visited[neighbor] = current
                    if neighbor in other_visited:
                        meeting_point = neighbor
                        break
                    current_queue.append(neighbor)
            if meeting_point is not None:
                break
        if meeting_point is not None:
            break

    if meeting_point is None:
        return None

    path_start = []
    curr = meeting_point
    while curr is not None:
        path_start.append(curr)
        curr = visited_start[curr]
    path_start.reverse()

    path_end = []
    curr = meeting_point
    while curr is not None:
        path_end.append(curr)
        curr = visited_end[curr]

    full_path = path_start + path_end[1:]
    return full_path

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_point = (0, 0)
    end_point = (4, 4)
    result = bidirectional_bfs(sample_grid, start_point, end_point)
    print(result)