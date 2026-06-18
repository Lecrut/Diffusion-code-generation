def is_larger(a: float, b: float) -> bool:
    """Returns True if a is strictly larger than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    result1 = is_larger(5.0, 3.0)
    print(f"is_larger(5.0, 3.0) = {result1}")

    result2 = is_larger(4.7, 4.8)
    print(f"is_larger(4.7, 4.8) = {result2}")

    result3 = is_larger(-10.5, -9.2)
    print(f"is_larger(-10.5, -9.2) = {result3}")

    # Test with integers as well (Python handles numeric types uniformly for this comparison).
    int_result = is_larger(7, 6)
    print(f"is_larger(7, 6) = {int_result}")