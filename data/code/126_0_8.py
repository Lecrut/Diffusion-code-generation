EQUALITY_CHECK_MSG = 'Both arguments must be int, float, or str'

def is_equal(a, b):
    if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
        raise ValueError(EQUALITY_CHECK_MSG)
    return a == b
if __name__ == '__main__':
    print(is_equal(5, 5))
    print(is_equal(10, 5))
    print(is_equal('hello', 'hello'))
    print(is_equal(1, 2))