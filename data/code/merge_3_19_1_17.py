def is_greater(a: any, b: any) -> bool:
    """Return True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    result1 = is_greater(5.0, 3.0)
    result2 = is_greater("apple", "banana")
    print(f"Test case 1 ({result1})")