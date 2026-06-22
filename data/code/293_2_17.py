def calculate_area(shape_type, *args):
    if shape_type == 'circle':
        radius = args[0]
        return 3.14159 * radius ** 2
    elif shape_type == 'square':
        side = args[0]
        return side ** 2
    elif shape_type == 'rectangle':
        length, width = args
        return length * width
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    print(calculate_area('circle', 5))
    print(calculate_area('square', 4))
    print(calculate_area('rectangle', 3, 7))