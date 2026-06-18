def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without external input.
    result1 = is_greater(10, 5)
    print(result1)

    result2 = is_greater(3.14, 2.718)
    print(result2)

    result3 = is_greater(100, 99)
    print(result3)

    result4 = is_greater(-5, -10)
    print(result4)