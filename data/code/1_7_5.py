import functools
def validate_and_normalize_weight(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise TypeError("Weight function requires at least one argument.")
        weight_input = args[0]
        if not isinstance(weight_input, (int, float)):
            raise TypeError(f"Weight must be a number, got {type(weight_input).__name__}")
        if weight_input < 0:
            raise ValueError("Weight cannot be negative.")
        normalized_weight = weight_input * 1.0                                
        result = func(*([normalized_weight] + list(args[1:])), **kwargs)
        return result
    return wrapper
@validate_and_normalize_weight
def calculate_area(weight, length):
    return weight * length
if __name__ == '__main__':
    print("--- Test Case 1: Valid Input ---")
    try:
        result1 = calculate_area(10.5, 2)
        print(f"Result 1: {result1}")
    except (TypeError, ValueError) as e:
        print(f"Error 1: {e}")
    print("\n--- Test Case 2: Invalid Type (String) ---")
    try:
        result2 = calculate_area("ten", 2)
        print(f"Result 2: {result2}")
    except (TypeError, ValueError) as e:
        print(f"Error 2: {e}")
    print("\n--- Test Case 3: Impossible Value (Negative) ---")
    try:
        result3 = calculate_area(-5, 10)
        print(f"Result 3: {result3}")
    except (TypeError, ValueError) as e:
        print(f"Error 3: {e}")
    print("\n--- Test Case 4: Missing Argument ---")
    try:
        result4 = calculate_area(10)
        print(f"Result 4: {result4}")
    except (TypeError, ValueError) as e:
        print(f"Error 4: {e}")
    print("\n--- Test Case 5: Valid Input (Integer) ---")
    try:
        result5 = calculate_area(5, 3)
        print(f"Result 5: {result5}")
    except (TypeError, ValueError) as e:
        print(f"Error 5: {e}")