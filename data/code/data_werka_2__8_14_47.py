import math

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        if len(args) != 2:
            raise ValueError("Rectangle requires two arguments: width and height")
        width, height = args
        return width * height
    elif shape_type == 'circle':
        if len(args) != 1:
            raise ValueError("Circle requires one argument: radius")
        radius = args[0]
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        if len(args) != 3:
            raise ValueError("Triangle requires three arguments: base and height")
        base, height = args
        return 0.5 * base * height
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 10, 5)
    circle_area = calculate_area('circle', 7)
    triangle_area = calculate_area('triangle', 8, 4)

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)
    print("Triangle Area:", triangle_area)