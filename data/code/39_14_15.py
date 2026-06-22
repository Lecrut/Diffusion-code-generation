def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_params = {
        "base_area_1": 20,
        "height_1": 10,
        "base_area_2": 5.5,
        "height_2": 3.2,
        "base_area_3": 100,
        "height_3": 0
    }
    volume_1 = calculate_prism_volume(test_params["base_area_1"], test_params["height_1"])
    volume_2 = calculate_prism_volume(test_params["base_area_2"], test_params["height_2"])
    volume_3 = calculate_prism_volume(test_params["base_area_3"], test_params["height_3"])
    print(volume_1)
    print(volume_2)
    print(volume_3)