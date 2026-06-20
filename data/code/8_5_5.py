def calculate_area(shape_type, **kwargs):
    if shape_type == 'rectangle':
        width = kwargs.get('width', 0)
        height = kwargs.get('height', 0)
        return width * height
    elif shape_type == 'circle':
        radius = kwargs.get('radius', 0)
        import math
        return math.pi * radius ** 2
    else:
        return 0

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', width=5, height=10)
    circle_area = calculate_area('circle', radius=7)
    print(rectangle_area)
    print(circle_area)