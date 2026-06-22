def is_float(value):
    return isinstance(value, float)

def compare_values(value1: float, value2: float) -> bool:
    if not is_float(value1):
        raise ValueError("The first input must be a float.")
    if not is_float(value2):
        raise ValueError("The second input must be a float.")
    return value1 > value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 3.14
    SAMPLE_VALUE_2 = 2.718
    result = compare_values(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)