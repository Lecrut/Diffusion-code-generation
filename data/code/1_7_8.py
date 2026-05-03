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
    def calculate_area(weight, length):
        return weight * length
    print("--- Testing valid inputs ---")
    try:
        result1 = calculate_area(10.5, 2)
        print(f"calculate_area(10.5, 2) = {result1}")
    except Exception as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_area(5, 10)
        print(f"calculate_area(5, 10) = {result2}")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Testing invalid data types ---")
    try:
        calculate_area("ten", 2)
    except TypeError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Testing impossible values (negative) ---")
    try:
        calculate_area(-5, 10)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Testing missing arguments ---")
    try:
        calculate_area(10)
    except TypeError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")