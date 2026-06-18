def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    assert is_even(4), "Should be True"
    assert not is_even(3), "Should be False"