def calculate_area(shape_type, *args):
    if shape_type == 'circle':
        radius = args[0]
        return math.pi * radius ** 2
    elif shape_type == 'square':
        side = args[0]
        return side ** 2
    elif shape_type == 'rectangle':
        length, width = args
        return length * width
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    print(f"Area of circle with radius 5: {calculate_area('circle', 5)}")
    print(f"Area of square with side 4: {calculate_area('square', 4)}")
    print(f"Area of rectangle with length 6 and width 3: {calculate_area('rectangle', 6, 3)}")