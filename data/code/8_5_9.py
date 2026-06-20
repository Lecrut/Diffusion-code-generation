import math

def calculate_area(shape_type, **dimensions):
    if shape_type == 'rectangle':
        width = dimensions.get('width', 0)
        height = dimensions.get('height', 0)
        return width * height
    elif shape_type == 'circle':
        radius = dimensions.get('radius', 0)
        return math.pi * radius ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', width=5, height=10)
    circle_area = calculate_area('circle', radius=7)
    print(rectangle_area)
    print(circle_area)