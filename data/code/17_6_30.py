def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(0) == True, "Test case 0 failed"
    assert is_even(1) == False, "Test case 1 failed"
    assert is_even(-1) == False, "Test case -1 failed"
    assert is_even(2) == True, "Test case 2 failed"
    assert is_even(-2) == True, "Test case -2 failed"
    assert is_even(3) == False, "Test case 3 failed"
    assert is_even(-3) == False, "Test case -3 failed"

if __name__ == '__main__':
    test_is_even()
    print("All test cases passed")