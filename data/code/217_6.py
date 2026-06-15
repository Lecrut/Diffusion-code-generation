def compare_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    if not isinstance(a, int) and not isinstance(b, int):
        return a > b
    try:
        result = a - b
        if result > 0:
            return True
        elif result < 0:
            return False
        else:
            return False
    except Exception as e:
        raise ValueError(f"Error during comparison: {e}")
if __name__ == '__main__':
    print(compare_numbers(5, 3))
    print(compare_numbers(5.0, 3))
    try:
        compare_numbers(5, "hello")
    except TypeError as e:
        print(f"Caught exception: {e}")
    try:
        compare_numbers("a", 3)
    except TypeError as e:
        print(f"Caught exception: {e}")