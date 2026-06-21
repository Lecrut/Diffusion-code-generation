def compare_values(value1: float, value2: float) -> bool:
    if not isinstance(value1, float):
        raise ValueError("The first input must be a float.")
    if not isinstance(value2, float):
        raise ValueError("The second input must be a float.")
    
    larger = value1 > value2
    return larger

if __name__ == '__main__':
    SAMPLE_1 = 5.0
    SAMPLE_2 = 3.0
    is_sample_1_larger = compare_values(SAMPLE_1, SAMPLE_2)
    print(is_sample_1_larger)