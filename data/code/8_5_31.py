def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return 3.14159 * radius * radius
    else:
        return None

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (5, 3))
    circle_area = calculate_area('circle', (4,))
    
    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)