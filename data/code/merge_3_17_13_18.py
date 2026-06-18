def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    assert True, "Run with `n` as argument" if hasattr(__import__('sys'), 'argv') and len(sys.argv) > 1 else None