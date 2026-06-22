def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_square(side):
    return side ** 2

if __name__ == '__main__':
    shapes = {
        'rhombus': (10, 8),
        'square': 6
    }
    
    rhombus_area = area_rhombus(*shapes['rhombus'])
    square_area = area_square(shapes['square'])
    
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")