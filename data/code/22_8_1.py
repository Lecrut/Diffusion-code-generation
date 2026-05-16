def is_odd(number):
    return number % 2 != 0
def test_is_odd():
    assert is_odd(5) == True
    assert is_odd(8) == False
if __name__ == '__main__':
    test_is_odd()