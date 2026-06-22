def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return 3.14159 * radius * radius
    else:
        return None

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (5, 3))
    circle_area = calculate_area('circle', (7,))
    
    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)