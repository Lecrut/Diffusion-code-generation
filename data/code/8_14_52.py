import math

def calculate_area(shape, *args):
    if shape == 'rectangle':
        if len(args) != 2:
            raise ValueError("Rectangle requires two arguments: width and height")
        width, height = args
        return width * height
    elif shape == 'circle':
        if len(args) != 1:
            raise ValueError("Circle requires one argument: radius")
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        if len(args) != 3:
            raise ValueError("Triangle requires three arguments: base, height, and side_length")
        base, height, side_length = args
        area = (base * height) / 2
        return area
    else:
        raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 5, 10)
    circle_area = calculate_area('circle', 7)
    triangle_area = calculate_area('triangle', 4, 6, 8)

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)
    print("Triangle Area:", triangle_area)