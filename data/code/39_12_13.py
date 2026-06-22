SHAPES = {
    "rectangular": {"width": 4, "depth": 5},
    "triangular": {"base": 6, "height_tri": 3},
}

def get_area(shape_type, params):
    if shape_type == "rectangular":
        return params["width"] * params["depth"]
    if shape_type == "triangular":
        return 0.5 * params["base"] * params["height_tri"]
    return 0

def calculate_prism_volume(shape_type, height, custom_params=None):
    params = custom_params if custom_params else SHAPES.get(shape_type, {})
    if not params:
        raise ValueError("Unknown shape or missing parameters")
    base_area = get_area(shape_type, params)
    return base_area * height

if __name__ == '__main__':
    volume = calculate_prism_volume("rectangular", 8)
    print(volume)
    volume_tri = calculate_prism_volume("triangular", 12)
    print(volume_tri)