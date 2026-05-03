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
def calculate_mass(weight):
    return weight * 100
if __name__ == '__main__':
    print("--- Testing valid input ---")
    try:
        result1 = calculate_mass(5.5)
        print(f"Input 5.5, Result: {result1}")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Testing invalid type input ---")
    try:
        calculate_mass("abc")
    except Exception as e:
        print(f"Caught expected error: {type(e).__name__}: {e}")
    print("\n--- Testing negative value input ---")
    try:
        calculate_mass(-10.0)
    except Exception as e:
        print(f"Caught expected error: {type(e).__name__}: {e}")
    print("\n--- Testing missing argument input ---")
    try:
        calculate_mass()
    except Exception as e:
        print(f"Caught expected error: {type(e).__name__}: {e}")