import math

def area_calculator(shape_type, dimensions):
    shape_map = {
        'square': lambda side: side * side,
        'rectangle': lambda length, width: length * width,
        'circle': lambda radius: math.pi * (radius ** 2)
    }
    
    if shape_type in shape_map:
        return shape_map[shape_type](*dimensions)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_area = area_calculator('square', [5])
    rectangle_area = area_calculator('rectangle', [4, 6])
    circle_area = area_calculator('circle', [3])

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")