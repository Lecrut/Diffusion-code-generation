from collections import deque

def bidirectional_bfs(start, end, grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and (grid[r][c] == 0)
    if not is_valid(start[0], start[1]) or not is_valid(end[0], end[1]):
        return None
    if start == end:
        return [start]
    queue_front = deque([start])
    queue_back = deque([end])
    visited_front = {start: None}
    visited_back = {end: None}
    meeting_point = None
    while queue_front and queue_back:
        if queue_front:
            curr = queue_front.popleft()
            if curr in visited_back:
                meeting_point = curr
                break
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = (curr[0] + dr, curr[1] + dc)
                if is_valid(nr, nc) and (nr, nc) not in visited_front:
                    visited_front[nr, nc] = curr
                    queue_front.append((nr, nc))
        if meeting_point:
            break
        if queue_back:
            curr = queue_back.popleft()
            if curr in visited_front:
                meeting_point = curr
                break
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = (curr[0] + dr, curr[1] + dc)
                if is_valid(nr, nc) and (nr, nc) not in visited_back:
                    visited_back[nr, nc] = curr
                    queue_back.append((nr, nc))
    if not meeting_point:
        return None
    path_front = []
    curr = meeting_point
    while curr is not None:
        path_front.append(curr)
        curr = visited_front[curr]
    path_back = []
    curr = meeting_point
    while curr is not None:
        path_back.append(curr)
        curr = visited_back[curr]
    path_front.reverse()
    path_back.pop(0)
    return path_front + path_back
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (4, 4)
    result = bidirectional_bfs(start, end, grid)
    print(result)