import heapq

def dijkstra_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    def get_cost(r, c):
        return grid[r][c]
    
    visited = set()
    heap = [(0, start)]
    parent = {start: None}
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while heap:
        cost, current = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == end:
            break
        
        cr, cc = current
        
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                neighbor_cost = get_cost(nr, nc)
                new_cost = cost + neighbor_cost
                
                if (nr, nc) not in parent or new_cost < parent[(nr, nc)][0]:
                    parent[(nr, nc)] = (new_cost, current)
                    heapq.heappush(heap, (new_cost, (nr, nc)))
    
    if end not in parent:
        return None, []
    
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr][1]
    
    path.reverse()
    
    return parent[end][0], path

if __name__ == '__main__':
    grid = [
        [1, 3, 1, 1],
        [1, 1, 4, 1],
        [1, 9, 1, 1],
        [1, 1, 1, 1]
    ]
    
    start_node = (0, 0)
    end_node = (3, 3)
    
    min_cost, path = dijkstra_shortest_path(grid, start_node, end_node)
    
    print(min_cost)
    print(path)