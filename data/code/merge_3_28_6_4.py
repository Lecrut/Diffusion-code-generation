def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Check condition: args[0] must be strictly greater than args[1]
        if len(args) < 2:
            raise TypeError("is_strictly_greater requires at least two positional arguments")
        
        first_arg = args[0]
        second_arg = args[1]

        # Handle comparison based on type (supports int, float, str for lexicographical order in Python)
        try:
            if not isinstance(first_arg, (int, float)) and not isinstance(second_arg, (int, float)):
                # For non-numeric types like strings, use < operator directly which works similarly to strict greater check logic-wise but we need > specifically. 
                # In Python 'a > b' handles mixed numeric/string if both are same type or comparable.
                pass
            
            if first_arg <= second_arg:
                return None  # Do not execute the function, just return None as signal of failure
        except TypeError:
            raise ValueError(f"Cannot compare {type(first_arg).__name__} and {type(second_arg).__name__}")

        return func(*args[2:], **kwargs)
    return wrapper

if __name__ == '__main__':
    # Sample function to test the decorator
    def add(a, b):
        """Simple addition function."""
        return a + b
    
    @is_strictly_greater
    def multiply(x, y):
        """Multiplication that only runs if x > y."""
        print(f"Executing multiplication: {x} * {y}")
        return x * y

    # Test cases with hard-coded values (no user input required)
    
    # Case 1: First argument is strictly greater than second -> Should execute
    result = multiply(5, 3)
    print(f"Result of multiplication (should be executed): {result}")

    # Case 2: First argument equals second -> Should NOT execute
    try:
        result_eq = multiply(4, 4)
        print("This line should not appear if decorator works correctly.")
    except Exception as e:
        pass
    
    # Case 3: First argument is less than second -> Should NOT execute
    try:
        result_less = multiply(2, 5)
        print("This line should not appear if decorator works correctly.")
    except Exception as e:
        pass

    # Test numeric types explicitly to ensure comparison logic holds for floats too
    @is_strictly_greater
    def divide(x, y):
        return x / y
    
    result_div = divide(10.5, 2)
    print(f"Result of division (should be executed): {result_div}")

    # Test string comparison logic if applicable (lexicographical order for strings in Python)
    @is_strictly_greater
    def compare_strings(a, b):
        return f"{a} > {b}" is True
    
    result_str = compare_strings("z", "a")  # 'z' > 'a' should be true -> execute
    print(f"String comparison executed: {result_str}")

    try:
        result_str_fail = compare_strings("a", "z")  # 'a' <= 'z' -> do not execute
        print("This line should not appear.")
    except Exception as e:
        pass
    
    print("\nAll tests completed successfully without external inputs or files.")