def safe_compare(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers for strict comparison.")
    if a != b:
        raise ValueError(f"Numbers are not equal: {a} != {b}")
    return True
if __name__ == '__main__':
    print("--- Test Case 1: Valid Integer Comparison ---")
    try:
        result = safe_compare(5, 5)
        print(f"Result: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")
    print("\n--- Test Case 2: Valid Float Comparison (Should raise TypeError for strict int check) ---")
    try:
        result = safe_compare(5.0, 5.0)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error caught: {e}")
    print("\n--- Test Case 3: Unequal Integer Comparison ---")
    try:
        safe_compare(10, 20)
    except ValueError as e:
        print(f"Error caught: {e}")
    except TypeError as e:
        print(f"Error caught: {e}")
    print("\n--- Test Case 4: Mixed Type Input (Should raise TypeError) ---")
    try:
        safe_compare(5, "5")
    except TypeError as e:
        print(f"Error caught: {e}")