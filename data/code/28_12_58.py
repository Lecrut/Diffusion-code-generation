def validate_float(value):
    if not isinstance(value, float):
        raise ValueError("Input must be a float.")

def compare_values(value1: float, value2: float) -> bool:
    validate_float(value1)
    validate_float(value2)
    return value1 > value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 3.14159
    SAMPLE_VALUE_2 = 2.71828
    result = compare_values(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)