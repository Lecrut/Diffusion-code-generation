def compute_prism_volume(base_area, height):
    result = base_area * height
    return result

if __name__ == '__main__':
    test_parameters = {
        "rectangular_prism": {"base_area": 40.0, "height": 15.0},
        "triangular_prism_alt": {"base_area": 22.5, "height": 9.0},
        "circular_prism_alt": {"base_area": 100.0, "height": 3.0}
    }
    for name, params in test_parameters.items():
        calculated_volume = compute_prism_volume(params["base_area"], params["height"])
        print(calculated_volume)