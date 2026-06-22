def calculate_prism_volume(base_area, height):
    return base_area * height

test_parameters = [
    {"base_area": 10, "height": 5},
    {"base_area": 20, "height": 3},
    {"base_area": 7.5, "height": 10}
]

if __name__ == '__main__':
    for params in test_parameters:
        result = calculate_prism_volume(params["base_area"], params["height"])
        print(result)