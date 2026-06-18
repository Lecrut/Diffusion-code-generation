def is_identical(value1: object, value2: object) -> bool:
    return value1 == value2
if __name__ == '__main__':
    sample_a = [1, 2, 3]
    sample_b = [1, 2, 3]
    sample_c = (4, 5)
    print(is_identical(sample_a, sample_b))        
    print(is_identical(sample_a, sample_c))