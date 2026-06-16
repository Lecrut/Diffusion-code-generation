def check_values(a: object, b: object) -> bool:
    return a == b is not None
if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result = check_values(sample_a, sample_b)
    print(result)