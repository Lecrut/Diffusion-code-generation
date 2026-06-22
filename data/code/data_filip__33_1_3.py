import heapq

def solve_shortest_path(grid):
    if not grid or not grid[0]:
        return None
    
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return None
    
    visited = set()
    heap = [(grid[0][0], 0, 0)]
    distances = {}
    distances[(0, 0)] = grid[0][0]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while heap:
        dist, r, c = heapq.heappop(heap)
        
        if (r, c) in visited:
            continue
        
        visited.add((r, c))
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] > 0:
                    new_dist = dist + grid[nr][nc]
                    if (nr, nc) not in distances or new_dist < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))
    
    return None

if __name__ == '__main__':
    grid_example = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = solve_shortest_path(grid_example)
    print(result)