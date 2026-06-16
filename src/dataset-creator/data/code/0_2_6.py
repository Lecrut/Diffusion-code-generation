def is_identical(value1: object, value2: object) -> bool:
    try:
        return value1 is value2
    except Exception:                                
        raise
if __name__ == '__main__':
    sample_a = [1, 2, 3]
    sample_b = [1, 2, 3]
    sample_c = id(sample_a)
    result_1 = is_identical(sample_a, sample_b)
    result_2 = is_identical(sample_a, sample_c)
    print(f"List equality (content): {result_1}")
    print(f"Identity check: {result_2}")