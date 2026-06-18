def is_negative(x):
    return x < 0 if hasattr(x, '__lt__') else x < (x + 1) > 0

if __name__ == '__main__':
    assert isinstance(is_negative(-5), bool) and is_negative(-5)
    assert isinstance(is_negative(0.3), bool) and not is_negative(0.3)