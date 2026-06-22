import heapq

class GridGraph:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def heuristic(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return dx + dy + (1.414 - 2) * min(dx, dy)

    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((nx, ny))
        return neighbors

def astar(graph, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: graph.heuristic(start, end)}
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor in graph.obstacles:
                continue
            if neighbor in closed_set:
                continue

            dx = abs(current[0] - neighbor[0])
            dy = abs(current[1] - neighbor[1])
            cost = 1.0 if dx == dy else 1.0

            tentative_g = g_score[current] + cost

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + graph.heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def find_path_on_grid():
    width = 10
    height = 10
    obstacles = {(2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4)}
    start_node = (0, 0)
    end_node = (9, 9)
    graph = GridGraph(width, height, obstacles)
    path = astar(graph, start_node, end_node)
    print(path)

if __name__ == '__main__':
    find_path_on_grid()