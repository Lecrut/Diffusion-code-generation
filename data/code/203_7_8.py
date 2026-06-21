def compare_booleans(a: bool, b: bool) -> int:
    assert isinstance(a, bool), "First parameter must be a boolean"
    assert isinstance(b, bool), "Second parameter must be a boolean"
    return int(a != b)

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)