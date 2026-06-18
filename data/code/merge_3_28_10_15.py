def is_larger(a: float | int, b: float | int) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no user input required)
    print(is_larger(5.0, 3))      # Expected: True
    print(is_larger(10, 9))       # Expected: True
    print(is_larger(2, 7))        # Expected: False
    print(is_larger(-1, -5))      # Expected: True