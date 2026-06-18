import heapq
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_score = float('inf')
        self.f_score = 0
        self.parent = None
    def __lt__(self, other):
        return self.f_score < other.f_score
def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)
def a_star(grid, start_x, start_y, goal_x, goal_y):
    open_set = []
    heapq.heappush(open_set, Node(start_x, start_y))
    grid[start_x][start_y] = 0
    while open_set:
        current_node = heapq.heappop(open_set)
        x, y = current_node.x, current_node.y
        if (x == goal_x and y == goal_y):
            path = []
            while current_node.parent is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return list(reversed(path))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (nx < 0 or ny < 0) or nx >= len(grid[0]) or ny >= len(grid):
                    continue
                cell_value = grid[nx][ny]
                if cell_value != -1:
                    temp_g_score = current_node.g_score + 1
                    if temp_g_score < grid[nx][ny]:
                        new_node = Node(nx, ny)
                        new_node.parent = current_node
                        new_node.g_score = temp_g_score
                        new_node.f_score = temp_g_score + heuristic(new_node, (goal_x, goal_y))
                        heapq.heappush(open_set, new_node)
                        grid[nx][ny] = 0
if __name__ == '__main__':
    map_data = [
        [-1, -1, -1, -1],
        [-1, -2, -3, -4],
        [-5, -6, -7, -8],
        [-9, 0, 1, 2]
    ]
    start_x = 1
    start_y = 1
    goal_x = 2
    goal_y = 2
    path = a_star(map_data, start_x, start_y, goal_x, goal_y)
    print(path)