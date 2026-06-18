def compare_values():
    """Compares two values based on exact type match and value equality."""
    
    def is_equal(val1, val2):
        # Prioritize exact type matching followed by direct comparison of values
        if not (type(val1) == type(val2)):
            return False
        
        try:
            result = val1 == val2
            
            # Handle boolean edge cases where True and 1 are technically equal but different types in some contexts, 
            # though Python treats them as same value. The prompt asks for exact TYPE matching first.
            # In strict type checking without coercion (int vs float):
            if isinstance(val1, bool) or isinstance(val2, bool):
                return False
            
            return result
            
        except TypeError:
            # If comparison itself fails due to incompatible types despite same declared type structure (rare), fall back
            try:
                val1 == val2 
            except Exception as e:
                print(f"Comparison error occurred in is_equal for input values. Type mismatch detected.")
                return False
        
        if not result:
            raise TypeError("Type Mismatch")

    # Hard-coded sample values to run without user interaction
    value_a = 10
    value_b = "10"

    print(f"{value_a} (type={type(value_a).__name__}) vs {value_b} (type={type(value_b).__name__}): Equal?")
    
    # Attempt comparison and report result based on type check logic in is_equal function
    
    try:
        if is_equal(value_a, value_b):
            print("Result: True")
        else:
            raise TypeError()
            
    except (TypeError) as e:
        print(f"Type Mismatch or Comparison Failure. {e}")

if __name__ == '__main__':
    compare_values()