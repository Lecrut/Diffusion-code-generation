from collections import deque

def bidirectional_bfs(grid, start, end):
    if not grid or not grid[0]:
        return (None, -1)
    rows = len(grid)
    cols = len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return (None, -1)
    if start == end:
        return ([start], 0)
    rows_offset = [-1, 1, 0, 0]
    cols_offset = [0, 0, -1, 1]
    front_start = deque([start])
    front_end = deque([end])
    visited_start = {start: None}
    visited_end = {end: None}
    meet_node = None
    while front_start and front_end:
        if len(front_start) <= len(front_end):
            is_start_expanding = True
        else:
            is_start_expanding = False
        if is_start_expanding:
            current = front_start.popleft()
            visited = visited_start
            opposite_visited = visited_end
            frontier = front_start
        else:
            current = front_end.popleft()
            visited = visited_end
            opposite_visited = visited_start
            frontier = front_end
        curr_r, curr_c = current
        for i in range(4):
            next_r = curr_r + rows_offset[i]
            next_c = curr_c + cols_offset[i]
            if 0 <= next_r < rows and 0 <= next_c < cols and (grid[next_r][next_c] == 0):
                neighbor = (next_r, next_c)
                if neighbor in opposite_visited:
                    if is_start_expanding:
                        meet_node = neighbor
                        break
                    else:
                        meet_node = neighbor
                        break
                if neighbor not in visited:
                    visited[neighbor] = current
                    frontier.append(neighbor)
        if meet_node is not None:
            break
    if meet_node is None:
        return (None, -1)
    path_from_start = []
    node = meet_node
    while node is not None:
        path_from_start.append(node)
        node = visited_start[node]
    path_from_start.reverse()
    path_from_end = []
    node = meet_node
    while node is not None:
        path_from_end.append(node)
        node = visited_end[node]
    full_path = path_from_start + path_from_end[1:]
    length = len(full_path) - 1
    return (full_path, length)
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (4, 4)
    path, distance = bidirectional_bfs(grid, start, end)
    print(path)
    print(distance)