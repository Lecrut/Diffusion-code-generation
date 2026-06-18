def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    assert are_equal(10, 10) is True
    assert are_equal([1, 2], [1, 2]) is True
    assert are_equal("hello", "world") is False
    print("All tests passed.")