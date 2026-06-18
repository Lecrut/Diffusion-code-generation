def is_zero(number):
    """
    Check if a given input number is exactly zero.
    
    Args:
        number (int | float | Decimal): The value to check.
        
    Returns:
        bool: True if the number is equal to 0, False otherwise.
    """
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -1, 1, 3.14, 0.0, "0", None]

    print("Testing is_zero function:")
    
    # Note: The type check below prevents non-numeric inputs from being evaluated directly 
    # to avoid runtime errors in a robust script, though the core logic only checks == 0.
    for val in test_values:
        try:
            result = is_zero(val) if isinstance(val, (int, float)) else "Value not numeric"
            print(f"is_zero({val!r}) -> {result}")
        except Exception as e:
            # Fallback for unexpected types like None that might cause issues in strict equality 
            # depending on implementation details, though Python's == 0 works with int/float.
            if val is not None and isinstance(val, (int, float)):
                result = False
            else:
                # For non-numeric or invalid inputs we treat them as not zero for safety in this context
                print(f"is_zero({val!r}) -> Error handling applied") 
        except TypeError:
             if val is None:
                 print(f"is_zero(None) -> Not exactly zero (None)")
             else:
                 result = False

    # Explicit demonstration with the core logic on valid numbers only to ensure correctness
    explicit_samples = [0, 1.5, -42]
    print("\nExplicit numeric samples:")
    for val in explicit_samples:
        if is_zero(val):
            print(f"{val} IS zero.")
        else:
            print(f"{val} IS NOT zero.")