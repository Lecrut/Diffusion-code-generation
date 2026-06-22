import heapq
from typing import List, Tuple, Optional, Dict

def get_shortest_path(
    grid: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int]
) -> Optional[List[Tuple[int, int]]]:
    rows = len(grid)
    if rows == 0:
        return None
    cols = len(grid[0])
    if cols == 0:
        return None
    
    start_r, start_c = start
    end_r, end_c = end
    
    if not (0 <= start_r < rows and 0 <= start_c < cols):
        return None
    if not (0 <= end_r < rows and 0 <= end_c < cols):
        return None
    
    if grid[start_r][start_c] == -1 or grid[end_r][end_c] == -1:
        return None
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    distances: Dict[Tuple[int, int], int] = {start: grid[start_r][start_c]}
    previous: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
    heap = [(grid[start_r][start_c], start)]
    visited = set()
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        curr_r, curr_c = current_node
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == end:
            break
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == -1:
                    continue
                neighbor = (nr, nc)
                weight = grid[nr][nc]
                new_dist = current_dist + weight
                
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (new_dist, neighbor))
    
    if end not in distances:
        return None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return path

if __name__ == '__main__':
    sample_grid = [
        [0, 1, 1, 1],
        [1, -1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
    ]
    start_pos = (0, 0)
    end_pos = (3, 3)
    result = get_shortest_path(sample_grid, start_pos, end_pos)
    print(result)