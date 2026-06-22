def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_params = {
        'base_area': 10.0,
        'height': 5.0
    }
    volume = calculate_prism_volume(test_params['base_area'], test_params['height'])
    print(volume)