def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_parameters = {
        'base_area': 50,
        'height': 12
    }
    base = test_parameters['base_area']
    h = test_parameters['height']
    volume = calculate_prism_volume(base, h)
    print(volume)