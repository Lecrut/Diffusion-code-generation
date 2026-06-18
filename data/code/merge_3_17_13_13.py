def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    assert is_even(4) is True and is_even(5) is False