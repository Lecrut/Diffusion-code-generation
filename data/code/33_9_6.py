import heapq
from typing import List, Tuple, Optional

class Node:
    def __init__(self, x: int, y: int, parent: Optional['Node'] = None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other: 'Node') -> bool:
        return self.f < other.f

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y

    def get_path(self) -> List[Tuple[int, int]]:
        path = []
        current = self
        while current is not None:
            path.append((current.x, current.y))
            current = current.parent
        return path[::-1]

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return dx + dy + (1.414 - 2) * min(dx, dy)

def get_neighbors(node: Node, grid_width: int, grid_height: int) -> List[Node]:
    neighbors = []
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    for dx, dy in directions:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            neighbors.append(Node(nx, ny, node))
    return neighbors

def a_star(
    grid_width: int,
    grid_height: int,
    start: Tuple[int, int],
    goal: Tuple[int, int],
    obstacles: List[Tuple[int, int]]
) -> Optional[List[Tuple[int, int]]]:
    if start[0] < 0 or start[1] < 0 or goal[0] < 0 or goal[1] < 0:
        return None
    if start[0] >= grid_width or start[1] >= grid_height or goal[0] >= grid_width or goal[1] >= grid_height:
        return None
    if start in obstacles or goal in obstacles:
        return None

    obstacle_set = set(obstacles)
    open_set = []
    closed_set = set()

    start_node = Node(start[0], start[1])
    start_node.g = 0
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g + start_node.h
    heapq.heappush(open_set, start_node)

    while open_set:
        current = heapq.heappop(open_set)
        if (current.x, current.y) in closed_set:
            continue
        if (current.x, current.y) == goal:
            return current.get_path()

        closed_set.add((current.x, current.y))

        for neighbor in get_neighbors(current, grid_width, grid_height):
            if (neighbor.x, neighbor.y) in closed_set:
                continue
            if (neighbor.x, neighbor.y) in obstacle_set:
                continue

            tentative_g = current.g + 1
            if neighbor.parent is not None:
                dx = neighbor.x - current.x
                dy = neighbor.y - current.y
                if dx != 0 and dy != 0:
                    tentative_g = current.g + 1.414
                else:
                    tentative_g = current.g + 1

            neighbor.g = tentative_g
            neighbor.h = heuristic((neighbor.x, neighbor.y), goal)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current
            heapq.heappush(open_set, neighbor)

    return None

if __name__ == '__main__':
    width = 10
    height = 10
    start_point = (0, 0)
    goal_point = (8, 7)
    obstacle_list = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]

    result_path = a_star(width, height, start_point, goal_point, obstacle_list)
    print(result_path)