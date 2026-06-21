def compare_values(value1: float, value2: float) -> bool:
    if not isinstance(value1, float):
        raise ValueError("The first input must be a float.")
    if not isinstance(value2, float):
        raise ValueError("The second input must be a float.")
    
    return value1 > value2

if __name__ == '__main__':
    first_sample = 5.0
    second_sample = 2.8
    is_first_greater = compare_values(first_sample, second_sample)
    print(is_first_greater)