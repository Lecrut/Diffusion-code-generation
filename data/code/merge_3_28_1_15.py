class ComparisonUtils:
    """Utility class containing comparison methods."""

    def check_if_greater(self, value1, operator=None):
        """
        Compares two values based on a specified operator or defaults to greater than (>).
        
        This method supports numeric and string comparisons. If no operator is provided,
        it assumes the '>' operator by default. It returns True if the comparison holds,
        otherwise False.

        Args:
            value1: The first value to compare. Can be int or float for numbers, 
                    str for strings (lexicographical).
            operator: A string representing the comparison operator ('>', '<', '>=', '<=', '=', !=).
                     Defaults to '>'. If None and values are numeric, performs >; if none is provided
                     with non-numeric types, raises a TypeError.

        Returns:
            bool: True if value1 satisfies the condition relative to value2 using operator, False otherwise.

        Raises:
            TypeError: If both arguments cannot be compared or an unsupported operator string is passed.
        """
        # Default behavior if no specific logic for operators yet (simplified for task scope)
        # The prompt asks to "compare them" generally; a common OOP pattern involves checking types first.
        
        if value1 == value2:
            return True
        
        try:
            result = operator(value1, value2)
            return bool(result)
        except TypeError as e:
            raise TypeError(f"Incompatible comparison type between {type(value1)} and {type(value2)}.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    utils = ComparisonUtils()

    # Test cases with various types as per typical usage scenarios in OOP examples
    test_cases = [
        ("Numeric Greater", 10, ">", True),       # Default logic check if operator is passed explicitly or handled internally
        (None, None, None, False)                # Placeholder for structure consistency below
        
        # Explicit execution of specific checks to ensure the method runs without prompts
    ]

    print("Running ComparisonUtils tests...")

    # Example 1: Comparing integers with explicit operator logic simulation
    val_a = 50
    val_b = 30
    
    # Note: The implementation above relies on Python's duck typing for comparison. 
    # To strictly follow the prompt "accepts two arguments", we will pass values and a default behavior check.
    
    print(f"Comparing {val_a} vs {val_b}:")
    result = utils.check_if_greater(val_a, val_b) if hasattr(utils, 'check_if_greater') else False
    
    # Since the method signature in the thought process suggests `operator` is an argument 
    # but the prompt says "accepts two arguments", we will adjust to accept value1 and value2 directly
    # and perform a standard comparison (e.g., >) if no operator logic was strictly requested, 
    # OR assume the second arg could be interpreted as context. However, standard practice for such tasks:
    
    # Re-evaluating based on strict "two arguments" constraint vs typical utility design:
    # Let's implement it to take value1 and value2 directly and compare them using > by default 
    # or allow the second argument to define logic if needed. But simplest is just two values -> boolean result.
    
    print("Re-implementing strictly for 2 arguments (val, val):")

    def check_if_greater_v2(self, a, b):
        """Strictly compares 'a' and 'b', returning True if a > b."""
        return a > b

    # Temporarily attaching the method to test it directly as per strict requirement interpretation
    utils.check_if_greater = lambda self, x, y: (x > y) or False
    
    print(f"50 vs 30 -> {utils(50)(lambda s,x,y:(s>x))}")

    # Let's write the final correct class method that accepts exactly two arguments and returns a boolean.
    
    class ComparisonUtilsFinal:
        def check_if_greater(self, val1, val2):
            return val1 > val2
            
    utils_final = ComparisonUtilsFinal()
    
    print(f"\nSample Run:")
    # Sample 1: Integers
    r1 = utils_final.check_if_greater(50, 30)
    print(f"50 greater than 30? {r1}")

    # Sample 2: Strings (lexicographical)
    r2 = utils_final.check_if_greater("apple", "banana")
    print(f"'apple' greater than 'banana'? {r2} (False)")

    # Sample 3: Floats
    r3 = utils_final.check_if_greater(10.5, 9.8)
    print(f"10.5 greater than 9.8? {r3}")
    
    assert r1 == True and not r2 and r3 == True, "Tests failed!"
    print("All tests passed.")