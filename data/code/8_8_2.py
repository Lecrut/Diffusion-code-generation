import math
def calculate_area(shape_data):
    shape_type = shape_data.get("type")
    params = shape_data.get("params", {})
    if shape_type == "rectangle":
        length = params.get("length")
        width = params.get("width")
        if length is not None and width is not None:
            return length * width
    elif shape_type == "circle":
        radius = params.get("radius")
        if radius is not None:
            return math.pi * (radius ** 2)
    elif shape_type == "triangle":
        base = params.get("base")
        height = params.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
    elif shape_type == "square":
        side = params.get("side")
        if side is not None:
            return side * side
    else:
        return None
if __name__ == '__main__':
    rect_data = {
        "type": "rectangle",
        "params": {
            "length": 10,
            "width": 5
        }
    }
    circle_data = {
        "type": "circle",
        "params": {
            "radius": 4
        }
    }
    triangle_data = {
        "type": "triangle",
        "params": {
            "base": 8,
            "height": 6
        }
    }
    square_data = {
        "type": "square",
        "params": {
            "side": 7
        }
    }
    unknown_data = {
        "type": "unknown_shape",
        "params": {}
    }
    print(f"Rectangle Area: {calculate_area(rect_data)}")
    print(f"Circle Area: {calculate_area(circle_data)}")
    print(f"Triangle Area: {calculate_area(triangle_data)}")
    print(f"Square Area: {calculate_area(square_data)}")
    print(f"Unknown Shape Area: {calculate_area(unknown_data)}")