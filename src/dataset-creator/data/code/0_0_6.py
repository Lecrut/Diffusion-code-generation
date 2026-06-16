def check_values(a: object, b: object) -> bool:
    return a == b is not None
if __name__ == '__main__':
    sample1 = 42
    sample2 = "Hello"
    result_match = check_values(sample1, sample2)
    print(result_match)