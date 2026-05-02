def calculate_area(shape_type, **kwargs):
    if shape_type == "rectangle":
        try:
            length = kwargs['length']
            width = kwargs['width']
            return length * width
        except KeyError:
            return "Error: Missing length or width for rectangle"
    elif shape_type == "circle":
        try:
            radius = kwargs['radius']
            return 3.141592653589793 * radius**2
        except KeyError:
            return "Error: Missing radius for circle"
    elif shape_type == "triangle":
        try:
            base = kwargs['base']
            height = kwargs['height']
            return 0.5 * base * height
        except KeyError:
            return "Error: Missing base or height for triangle"
    else:
        return "Error: Invalid shape type specified"
if __name__ == '__main__':
    print(calculate_area("rectangle", length=10, width=5))
    print(calculate_area("circle", radius=4))
    print(calculate_area("triangle", base=8, height=4))
    print(calculate_area("square", side=5))
    print(calculate_area("rectangle", length=7, width=3))
    print(calculate_area("circle", radius=10))
    print(calculate_area("triangle", base=6, height=5))