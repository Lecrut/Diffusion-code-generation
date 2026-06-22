def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return 3.14159 * (radius ** 2)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (5, 10))
    circle_area = calculate_area('circle', (7,))
    print(rectangle_area)
    print(circle_area)