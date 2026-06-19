def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(0) == True, "Test case for zero failed"
    assert is_even(1) == False, "Test case for positive odd number failed"
    assert is_even(2) == True, "Test case for positive even number failed"
    assert is_even(-1) == False, "Test case for negative odd number failed"
    assert is_even(-2) == True, "Test case for negative even number failed"

if __name__ == '__main__':
    test_is_even()
    print(is_even(0))
    print(is_even(3))
    print(is_even(-4))