import functools
def validate_and_normalize_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise TypeError("Weight function requires at least one argument.")
        weight = args[0]
        if not isinstance(weight, (int, float)):
            raise TypeError(f"Weight must be a number, got {type(weight).__name__}")
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        normalized_weight = weight
        result = func(*args, **kwargs)
        return result
    return wrapper
if __name__ == '__main__':
    @validate_and_normalize_weight
    def calculate_area(weight):
        return weight * 10
    print("--- Testing valid inputs ---")
    try:
        result1 = calculate_area(10.5)
        print(f"Input 10.5, Result: {result1}")
        result2 = calculate_area(0)
        print(f"Input 0, Result: {result2}")
    except Exception as e:
        print(f"Unexpected error during valid test: {e}")
    print("\n--- Testing invalid data types ---")
    try:
        calculate_area("invalid")
    except TypeError as e:
        print(f"Caught expected error for string input: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Testing impossible values (negative) ---")
    try:
        calculate_area(-5.0)
    except ValueError as e:
        print(f"Caught expected error for negative input: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Testing missing arguments ---")
    try:
        calculate_area()
    except TypeError as e:
        print(f"Caught expected error for missing argument: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")