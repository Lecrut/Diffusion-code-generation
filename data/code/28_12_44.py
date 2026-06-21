def compare_values(value1: float, value2: float) -> bool:
    if not isinstance(value1, float):
        raise ValueError("The first input must be a float.")
    if not isinstance(value2, float):
        raise ValueError("The second input must be a float.")
    
    return value1 > value2

if __name__ == '__main__':
    SAMPLE_THRESHOLD = 0.0
    SAMPLE_VALUE_1 = 3.14 + SAMPLE_THRESHOLD
    SAMPLE_VALUE_2 = 2.71 + SAMPLE_THRESHOLD
    
    result = compare_values(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)