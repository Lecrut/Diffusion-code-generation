def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    test_parameters = {
        "square_base_prism": {"base_area": 25, "height": 10},
        "triangular_base_prism": {"base_area": 15.5, "height": 8},
        "circular_base_prism": {"base_area": 50.24, "height": 12}
    }

    for test_name, params in test_parameters.items():
        volume = calculate_prism_volume(params["base_area"], params["height"])
        print(volume)