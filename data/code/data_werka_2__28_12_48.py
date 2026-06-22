def compare_values(value1: float, value2: float) -> bool:
    if not isinstance(value1, float):
        raise ValueError("The first input must be a float.")
    if not isinstance(value2, float):
        raise ValueError("The second input must be a float.")
    return value1 > value2

if __name__ == '__main__':
    sample_values = {
        'first_value': 3.14,
        'second_value': 2.71
    }
    result = compare_values(sample_values['first_value'], sample_values['second_value'])
    print(result)