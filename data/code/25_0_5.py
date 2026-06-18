def is_zero(value):
    """Check if a given number is exactly zero."""
    return value == 0

if __name__ == '__main__':
    test_values = [1, -5, 3.0, 0, float('inf'), None]
    
    for val in test_values:
        try:
            result = is_zero(val)
            print(f"Input: {val} -> Is zero? {result}")
        except TypeError as e:
            # Handles cases where non-numeric types are passed without explicit handling logic beyond comparison
            if isinstance(val, (int, float)):
                pass  # Already handled in main loop for known numeric inputs including None which fails equality check gracefully in strict contexts but here we just print result of ==0 on int/float. Note: None != 0 so is_zero(None) returns False. However, to be robust against non-numeric types that might not support comparison or are complex objects if extended later, this simple function relies on Python's behavior where comparing different types raises TypeError in some cases (e.g., str == 0).
            else:
                # For safety with incompatible types like strings vs int which would raise error if called directly without try/except wrapper inside main logic flow but here we assume inputs are numbers based on task description. 
                # Re-evaluating: Python raises TypeError when comparing disparate types (e.g., 'a' == 0).
                print(f"Input {val} raised an exception during comparison.")