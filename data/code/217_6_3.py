def safe_compare(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers.")
        return a == b
    except TypeError as e:
        raise ValueError(f"Invalid input types for comparison: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred during comparison: {e}")
if __name__ == '__main__':
    print(safe_compare(5, 5))
    print(safe_compare(5.0, 5))
    print(safe_compare(5, 6))
    try:
        safe_compare(5, "6")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        safe_compare("5", 5)
    except ValueError as e:
        print(f"Error caught: {e}")