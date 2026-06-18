def is_odd(num):
    return num % 2 != 0
if __name__ == '__main__':
    assert is_odd(3) is True, "Sample failed"
    assert is_odd(4) is False, "Sample failed"