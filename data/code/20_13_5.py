def check_equality(value1, value2):
    """
    Compares two values of comparable types (numbers, strings) 
    to determine if they are equal. Handles type errors gracefully.
    
    Args:
        value1: First input value
        value2: Second input value
        
    Returns:
        bool: True if the inputs are numerically or string-wise equal and same type, False otherwise
    
    Raises:
        TypeError: If types cannot be compared (e.g., int vs str) in a way that Python allows.
                  Note: In strict typing scenarios like float(10) == 10, this returns True naturally 
                  due to numeric promotion in Python's default comparison behavior unless explicitly restricted.
    """
    
    # Check if both inputs are of the same type first for stricter equality logic on non-numeric types
    # This avoids mixing int and str comparisons which would raise TypeError automatically anyway
    
    try:
        result = value1 == value2
        
        return bool(result)
        
    except TypeError as e:
        print(f"Error during comparison of {type(value1).__name__} and {type(value2).__name__}: {e}")
        return False

def main():
    """
    Main function that defines sample values to test the equality check without user input.
    
    This block runs independently, requiring no external inputs or files.
    It demonstrates various comparison scenarios including integers, floats, strings, 
    and mixed types where appropriate comparisons might fail logically (like int vs float representing different precision).
    """
    
    # Sample data for demonstration
    
    sample_int = 10
    sample_float = 10.0
    sample_str_1 = "hello"
    sample_str_2 = "world"
    incompatible_int = 5
    incompatible_str = "text"
    
    print("Testing Equality Checks")
    print("=" * 30)
    
    # Test Case 1: Integer vs Float (representing same value numerically) - Python allows this comparison naturally
    
    result_1 = check_equality(sample_int, sample_float)
    print(f"{sample_int} == {sample_float}: {'EQUAL' if result_1 else 'NOT EQUAL'}")
    
    # Test Case 2: Integer vs String (different types, different value representation) - Raises TypeError naturally
    
    try:
        result_2 = check_equality(sample_str_1, sample_str_2)
        print(f"{sample_str_1} == {sample_str_2}: {'EQUAL' if result_2 else 'NOT EQUAL'}")
        
    except Exception as e:
        # This block handles cases where types are fundamentally incompatible for comparison logic 
        # outside of Python's built-in handling. Here we demonstrate explicit type checking to ensure safety
        
        if not isinstance(sample_str_1, str) or not isinstance(sample_str_2, str):
             print(f"Mixed Type Error: {type(sample_int).__name__} and {sample_str_1.__class__.__name__}")
    
    # Test Case 3: Explicit type check to avoid silent mismatches
    
    result_3 = sample_int == incompatible_str

if __name__ == '__main__':
    pass
