def check_equality(value1: bool, value2: bool) -> bool:
    return value1 == value2

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = check_equality(sample_a, sample_b)
    print(result)