def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_parameters = {
        'rectangular_prism_1': {'base_area': 25.0, 'height': 10.0},
        'triangular_prism_1': {'base_area': 15.5, 'height': 8.0},
        'hexagonal_prism_1': {'base_area': 42.0, 'height': 12.5}
    }
    
    for name, params in test_parameters.items():
        volume = calculate_prism_volume(params['base_area'], params['height'])
        print(f'{name}: {volume}')