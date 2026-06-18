def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    assert are_equal([1, 2], [1, 2]) is True
    assert are_equal({'a': 1}, {'b': 1}) is False
    assert are_equal(5.0, 5) is True
    print("All tests passed.")