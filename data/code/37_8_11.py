def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    sample_cases = {
        "default": {"base": 7, "height": 4}
    }
    for case_name, params in sample_cases.items():
        result = calculate_parallelogram_area(params["base"], params["height"])
        print(result)