def calculate_area(shape_params):
    shape_type = shape_params.get("type")
    if shape_type == "rectangle":
        width = shape_params.get("width", 0)
        height = shape_params.get("height", 0)
        return width * height
    elif shape_type == "circle":
        radius = shape_params.get("radius", 0)
        return 3.141592653589793 * radius * radius
    elif shape_type == "triangle":
        base = shape_params.get("base", 0)
        height = shape_params.get("height", 0)
        return 0.5 * base * height
    elif shape_type == "trapezoid":
        base1 = shape_params.get("base1", 0)
        base2 = shape_params.get("base2", 0)
        height = shape_params.get("height", 0)
        return 0.5 * (base1 + base2) * height
    elif shape_type == "polygon":
        points = shape_params.get("points", [])
        if len(points) < 3:
            return 0.0
        area = 0.0
        n = len(points)
        for i in range(n):
            j = (i + 1) % n
            area += points[i][0] * points[j][1]
            area -= points[j][0] * points[i][1]
        return abs(area) / 2.0
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == "__main__":
    rect_params = {"type": "rectangle", "width": 5, "height": 10}
    circle_params = {"type": "circle", "radius": 3}
    triangle_params = {"type": "triangle", "base": 4, "height": 6}
    trapezoid_params = {"type": "trapezoid", "base1": 3, "base2": 7, "height": 5}
    square_params = {"type": "polygon", "points": [(0, 0), (4, 0), (4, 4), (0, 4)]}
    
    print(calculate_area(rect_params))
    print(calculate_area(circle_params))
    print(calculate_area(triangle_params))
    print(calculate_area(trapezoid_params))
    print(calculate_area(square_params))