def calculate_area(shape_type, **dimensions):
    shape_type_lower = shape_type.lower()
    if shape_type_lower == 'rectangle':
        width = dimensions.get('width')
        height = dimensions.get('height')
        if width is None or height is None:
            raise ValueError("Rectangle requires 'width' and 'height'.")
        return width * height
    elif shape_type_lower == 'circle':
        radius = dimensions.get('radius')
        if radius is None:
            raise ValueError("Circle requires 'radius'.")
        return 3.141592653589793 * (radius ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rect_area = calculate_area('rectangle', width=10, height=5)
    print(rect_area)
    circle_area = calculate_area('circle', radius=7)
    print(circle_area)