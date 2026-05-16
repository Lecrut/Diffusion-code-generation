def is_odd(number):
    return number % 2 != 0
def test_is_odd():
    assert is_odd(7) == True
    assert is_odd(4) == False
if __name__ == '__main__':
    test_is_odd()