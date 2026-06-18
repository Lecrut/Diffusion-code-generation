def is_larger(a: float, b: float) -> bool:
    """Returns True if a > b strictly False otherwise."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to verify functionality without external input.
    print(is_larger(10, 5))       # Expected: True
    print(is_larger(3.5, 4.2))   # Expected: False
    print(is_larger(-1, -2))     # Expected: True