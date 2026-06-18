def are_equal(item1: any, item2: any) -> bool:
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases covering integers, strings, and lists
    assert are_equal(42, 42) is True
    assert are_equal("hello", "hello") is True
    assert are_equal([1, 2, 3], [1, 2, 3]) is True
    # Cases that should return False
    assert are_equal(42, 43) is False
    assert are_equal("hi", "bye") is False
    assert are_equal([0, 1], [1, 0]) is False
    
    print("All sample tests passed.")