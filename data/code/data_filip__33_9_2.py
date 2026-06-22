import heapq
from typing import List, Tuple, Optional, Dict

class Node:
    def __init__(self, x: int, y: int, parent: Optional['Node']) -> None:
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

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class AStar:
    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.moves = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return 10 * max(dx, dy) + (14 if dx != 0 and dy != 0 else 0)

    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        if self.grid[start[1]][start[0]] == 1 or self.grid[end[1]][end[0]] == 1:
            return None
        
        start_node = Node(start[0], start[1], None)
        end_node = Node(end[0], end[1], None)
        
        open_list: List[Node] = [start_node]
        closed_set: set = set()
        
        while open_list:
            current_node = heapq.heappop(open_list)
            
            if (current_node.x, current_node.y) == (end_node.x, end_node.y):
                path = []
                while current_node:
                    path.append((current_node.x, current_node.y))
                    current_node = current_node.parent
                return list(reversed(path))
            
            closed_set.add((current_node.x, current_node.y))
            
            for move_x, move_y in self.moves:
                neighbor_x = current_node.x + move_x
                neighbor_y = current_node.y + move_y
                
                if not (0 <= neighbor_x < self.cols and 0 <= neighbor_y < self.rows):
                    continue
                
                if self.grid[neighbor_y][neighbor_x] == 1:
                    continue
                
                if (neighbor_x, neighbor_y) in closed_set:
                    continue
                
                move_cost = 10 if move_x == 0 or move_y == 0 else 14
                
                if move_x != 0 and move_y != 0:
                    if self.grid[current_node.y][current_node.x + move_x] == 1:
                        continue
                    if self.grid[current_node.y + move_y][current_node.x] == 1:
                        continue
                
                neighbor_node = Node(neighbor_x, neighbor_y, current_node)
                tentative_g = current_node.g + move_cost
                
                existing_node = None
                for node in open_list:
                    if node.x == neighbor_x and node.y == neighbor_y:
                        existing_node = node
                        break
                
                if existing_node is None:
                    neighbor_node.g = tentative_g
                    neighbor_node.h = self.heuristic((neighbor_x, neighbor_y), (end_node.x, end_node.y))
                    neighbor_node.f = neighbor_node.g + neighbor_node.h
                    heapq.heappush(open_list, neighbor_node)
                elif tentative_g < existing_node.g:
                    existing_node.g = tentative_g
                    existing_node.parent = current_node
                    existing_node.f = existing_node.g + existing_node.h

        return None

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    finder = AStar(grid)
    path = finder.find_path(start, end)
    print(path)