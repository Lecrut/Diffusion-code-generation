def is_odd(n: int) -> bool:
    return n % 2 != 0
if __name__ == '__main__':
    assert is_odd(3) is True
    assert is_odd(-15) is True
    assert is_odd(42) is False