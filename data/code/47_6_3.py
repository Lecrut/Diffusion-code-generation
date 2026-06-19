def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = {
        'A': (0, 0),
        'B': (4, 0),
        'C': (2, 3)
    }
    
    x1, y1 = vertices['A']
    x2, y2 = vertices['B']
    x3, y3 = vertices['C']
    
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    print(area)