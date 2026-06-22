def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = {
        'rectangular_base_1': {'base_area': 10.0, 'height': 5.0, 'expected_volume': 50.0},
        'triangular_base_1': {'base_area': 15.5, 'height': 4.0, 'expected_volume': 62.0},
        'hexagonal_base_1': {'base_area': 24.0, 'height': 8.0, 'expected_volume': 192.0}
    }

    for case_name, params in test_cases.items():
        calculated_volume = calculate_prism_volume(params['base_area'], params['height'])
        print(f"Case {case_name}: Calculated Volume = {calculated_volume}")