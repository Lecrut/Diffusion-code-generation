def calculate_area(shape_type, **kwargs):
    if shape_type == "rectangle":
        if 'length' in kwargs and 'width' in kwargs:
            return kwargs['length'] * kwargs['width']
        else:
            raise ValueError("Rectangle requires 'length' and 'width'")
    elif shape_type == "circle":
        if 'radius' in kwargs:
            import math
            return math.pi * (kwargs['radius'] ** 2)
        else:
            raise ValueError("Circle requires 'radius'")
    elif shape_type == "triangle":
        if 'base' in kwargs and 'height' in kwargs:
            return 0.5 * kwargs['base'] * kwargs['height']
        else:
            raise ValueError("Triangle requires 'base' and 'height'")
    else:
        raise ValueError(f"Invalid shape type: {shape_type}")
if __name__ == '__main__':
    print(calculate_area("rectangle", length=10, width=5))
    print(calculate_area("circle", radius=3))
    print(calculate_area("triangle", base=4, height=6))
    try:
        calculate_area("square", side=5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area("circle", side=5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area("rectangle", length=10)
    except ValueError as e:
        print(f"Error caught: {e}")