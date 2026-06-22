from collections import deque

def shortest_path(grid: list[list[int]]) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    if rows == 0 or cols == 0:
        return []
    
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return []
    
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    queue = deque()
    queue.append(start)
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    parent = {}
    parent[start] = None
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            break
        
        r, c = current
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                parent[(nr, nc)] = current
                queue.append((nr, nc))
    
    if end not in parent:
        return []
    
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    
    path.reverse()
    return path

if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0]
    ]
    result = shortest_path(grid)
    print(result)