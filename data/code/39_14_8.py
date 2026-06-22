def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = {
        "rectangular_base": {"base_area": 50.0, "height": 10.0},
        "triangular_base": {"base_area": 25.5, "height": 8.0},
        "hexagonal_base": {"base_area": 100.0, "height": 15.0}
    }
    for case_name, params in test_cases.items():
        volume = calculate_prism_volume(params["base_area"], params["height"])
        print(f"{case_name}: {volume}")