def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_parameters = {
        'base_area': 10.5,
        'height': 5.0
    }
    volume = calculate_prism_volume(test_parameters['base_area'], test_parameters['height'])
    print(volume)