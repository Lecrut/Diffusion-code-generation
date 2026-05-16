def calculate_area(shape_type, **kwargs):
    if shape_type == "rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        if length is not None and width is not None:
            return length * width
        else:
            raise ValueError("Missing length or width for rectangle")
    elif shape_type == "circle":
        radius = kwargs.get("radius")
        if radius is not None:
            return 3.141592653589793 * radius**2
        else:
            raise ValueError("Missing radius for circle")
    elif shape_type == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            raise ValueError("Missing base or height for triangle")
    else:
        raise ValueError(f"Invalid shape type: {shape_type}")
if __name__ == '__main__':
    print(calculate_area("rectangle", length=10, width=5))
    print(calculate_area("circle", radius=4))
    print(calculate_area("triangle", base=8, height=4))
    try:
        calculate_area("square", side=5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area("circle", radius=2)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area("rectangle", length=10)
    except ValueError as e:
        print(f"Error caught: {e}")