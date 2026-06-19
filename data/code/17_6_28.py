def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(0) == True, 'Test case 1 failed'
    assert is_even(1) == False, 'Test case 2 failed'
    assert is_even(-1) == False, 'Test case 3 failed'
    assert is_even(2) == True, 'Test case 4 failed'
    assert is_even(-2) == True, 'Test case 5 failed'
    assert is_even(100) == True, 'Test case 6 failed'
    assert is_even(-100) == True, 'Test case 7 failed'
    assert is_even(101) == False, 'Test case 8 failed'
    assert is_even(-101) == False, 'Test case 9 failed'
if __name__ == '__main__':
    test_is_even()
    print(is_even(0))
    print(is_even(5))
    print(is_even(-4))
    print(is_even(17))