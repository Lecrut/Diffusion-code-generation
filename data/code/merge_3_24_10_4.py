def is_negative(value):
    """
    Returns True if value is strictly less than zero, False otherwise.
    
    Args:
        value (int | float | complex): The numerical input to evaluate.
        
    Returns:
        bool: True if negative, False if non-negative or invalid type.
    """
    try:
        # Attempt conversion for potential string inputs without external dependencies
        num = int(value) if isinstance(value, str) else value
        
        # Handle complex numbers by checking the real part (standard practice unless specified otherwise)
        # However, strict 'less than' comparison only works reliably on ordered types.
        # We treat any non-integer float or integer as valid for ordering checks in Python 3.
        
        if isinstance(num, bool):
            return False
        
        if isinstance(num, (int, float)):
            return num < 0
        
        elif isinstance(num, complex):
            # For complex numbers, strictly less than is not defined mathematically.
            # By convention in many libraries, we check the real part or treat as non-negative for safety.
            # Here, to maintain robustness and avoid undefined behavior: return False if imaginary exists OR real >= 0
            # A safer interpretation of "negative" for mixed types usually defaults to checking real component < 0
            # But since strict ordering doesn't apply to complex, we ensure we don't raise TypeError.
            return num.real < 0
        
        else:
            # Fallback for unexpected but hashable-like inputs (e.g., some custom numeric objects)
            try:
                float(num)
            except (TypeError, ValueError):
                return False
    
    except Exception:
        # Catch any unforeseen conversion errors to ensure robustness without crashing
        return False

if __name__ == '__main__':
    test_cases = [-5, 0.1, -3.9, "hello", True, complex(2, 4), None]
    
    for case in test_cases:
        try:
            result = is_negative(case)
            print(f"is_negative({case!r}) = {result}")
        except Exception as e:
            print(f"Error processing {case}: {e}")