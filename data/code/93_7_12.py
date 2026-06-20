if __name__ == '__main__':
    a = False
    b = False
    try:
        assert isinstance(a, bool) and isinstance(b, bool)
        print(not a and not b)
    except AssertionError:
        print("Invalid input: both values must be boolean")