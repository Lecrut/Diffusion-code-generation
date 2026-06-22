def compare_values(value1: float, value2: float) -> bool:
    if not isinstance(value1, float):
        raise ValueError("The first input must be a float.")
    if not isinstance(value2, float):
        raise ValueError("The second input must be a float.")
    
    return value1 > value2

if __name__ == '__main__':
    VALUE_ONE = 5.0
    VALUE_TWO = 3.0
    comparison_result = compare_values(VALUE_ONE, VALUE_TWO)
    print(comparison_result)