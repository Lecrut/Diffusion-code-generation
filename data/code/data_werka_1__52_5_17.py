def calculate_polygon_area(dimensions):
    if len(dimensions) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    n = len(dimensions)
    area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        area += dimensions[i] * dimensions[j]
    
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon1 = [3, 4, 5]
    try:
        area1 = calculate_polygon_area(polygon1)
        print(f"Area of polygon with sides {polygon1}: {area1}")
    except ValueError as e:
        print(f"Error: {e}")
    
    polygon2 = [6, 8, 10, 12]
    try:
        area2 = calculate_polygon_area(polygon2)
        print(f"Area of polygon with sides {polygon2}: {area2}")
    except ValueError as e:
        print(f"Error: {e}")
    
    polygon3 = [1, 1]
    try:
        area3 = calculate_polygon_area(polygon3)
        print(f"Area of polygon with sides {polygon3}: {area3}")
    except ValueError as e:
        print(f"Error: {e}")