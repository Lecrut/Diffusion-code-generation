def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return 3.14159 * radius ** 2
    elif shape == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    triangle_dimensions = (8, 4)

    print("Rectangle Area:", calculate_area('rectangle', rectangle_dimensions))
    print("Circle Area:", calculate_area('circle', circle_dimensions))
    print("Triangle Area:", calculate_area('triangle', triangle_dimensions))