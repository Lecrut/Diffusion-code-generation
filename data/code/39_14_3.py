def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    test_parameters = {
        "rectangle_prism": {"base_area": 15.0, "height": 10.0},
        "triangle_prism": {"base_area": 7.5, "height": 6.0},
        "hexagonal_prism": {"base_area": 25.0, "height": 12.0}
    }
    for name, params in test_parameters.items():
        volume = calculate_prism_volume(params["base_area"], params["height"])
        print(f"{name}: {volume}")