import math

def calculate_area(shape_dict):
    shape_type = shape_dict.get("type")
    if shape_type == "circle":
        radius = shape_dict.get("radius", 0)
        return math.pi * radius ** 2
    elif shape_type == "rectangle":
        width = shape_dict.get("width", 0)
        height = shape_dict.get("height", 0)
        return width * height
    elif shape_type == "triangle":
        base = shape_dict.get("base", 0)
        height = shape_dict.get("height", 0)
        return 0.5 * base * height
    elif shape_type == "square":
        side = shape_dict.get("side", 0)
        return side ** 2
    elif shape_type == "ellipse":
        semi_major = shape_dict.get("semi_major", 0)
        semi_minor = shape_dict.get("semi_minor", 0)
        return math.pi * semi_major * semi_minor
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == "__main__":
    shapes = [
        {"type": "circle", "radius": 5},
        {"type": "rectangle", "width": 4, "height": 6},
        {"type": "triangle", "base": 3, "height": 4},
        {"type": "square", "side": 7},
        {"type": "ellipse", "semi_major": 5, "semi_minor": 3}
    ]
    for shape in shapes:
        print(calculate_area(shape))