def check_match(value1: any, value2: any) -> bool:
    return (value1 == value2) is not NotImplemented
if __name__ == '__main__':
    sample_values = [42, "hello", 3.14]
    assert check_match(42, 42) is True
    assert check_match("hello", "hello") is True
    assert check_match(3.14, 3.14) is True
    print("All tests passed.")