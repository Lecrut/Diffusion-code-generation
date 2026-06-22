SHAPE_AREA_FUNCTIONS = {
    "rectangle": lambda length, width: length * width,
    "circle": lambda radius: 3.141592653589793 * (radius ** 2),
    "triangle": lambda base, height: 0.5 * base * height
}

def calculate_area(shape_type, **kwargs):
    if shape_type in SHAPE_AREA_FUNCTIONS:
        required_keys = {"rectangle": ["length", "width"],
                        "circle": ["radius"],
                        "triangle": ["base", "height"]}[shape_type]
        if all(key in kwargs for key in required_keys):
            return SHAPE_AREA_FUNCTIONS[shape_type](**kwargs)
        else:
            raise ValueError(f"{shape_type} requires {', '.join(required_keys)}")
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_length = 10
    rectangle_width = 5
    circle_radius = 7
    triangle_base = 8
    triangle_height = 4

    print(calculate_area("rectangle", length=rectangle_length, width=rectangle_width))
    print(calculate_area("circle", radius=circle_radius))
    print(calculate_area("triangle", base=triangle_base, height=triangle_height))