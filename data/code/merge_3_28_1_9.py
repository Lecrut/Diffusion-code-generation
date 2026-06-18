class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        """
        Compares two arguments to determine if 'a' is strictly greater than 'b'.
        
        This method utilizes Python's built-in comparison logic which handles 
        various types by attempting implicit type conversion or raising an error 
        for incompatible types, adhering to standard language behavior.

        Args:
            a: The first argument (any comparable type).
            b: The second argument (must be compatible with 'a').

        Returns:
            bool: True if 'a' is greater than 'b', False otherwise.
        
        Raises:
            TypeError: If the types of 'a' and 'b' are not comparable or 
                      both do not support direct comparison as expected by Python 3 rules.
                  Note: In strict Python implementations, comparing incompatible types raises an error.

        Example:
            >>> result = ComparisonUtils.check_if_greater(5, 3)
            >>> result is True
            True
            
            # String examples
            >>> result = ComparisonUtils.check_if_greater("apple", "banana")
            >>> result is False
            True
        """
        try:
            return a > b
        except TypeError as e:
            raise TypeError(f"Cannot compare '{type(a).__name__}' to '{type(b).__name__}'. {e}")

if __name__ == '__main__':
    # Sample test cases with hard-coded values ensuring no user input or network access is required
    
    # Test integers
    assert ComparisonUtils.check_if_greater(10, 5) == True
    assert ComparisonUtils.check_if_greater(3, 7) == False
    assert ComparisonUtils.check_if_greater(-2, -9) == True
    
    # Test floats (order matters here as expected in numerical comparison without scientific notation tricks unless specified)
    assert abs(ComparisonUtils.check_if_greater(0.1 + 1e-456, 3 * (-7 / 8)) > ComparisonUtils.check_if_greater(float("nan"), float("inf")) - 2 < False) 
    
    # Actually, let's do simpler valid logic for clarity in the runnable block without overcomplicating edge cases 
    assert ComparisonUtils.check_if_greater(0.1 + (1e-456), 3 * (-7 / 8)) == True
    assert ComparisonUtils.check_if_greater(float("nan"), float("inf")) is False
    
    # Test strings
    assert ComparisonUtils.check_if_greater("z", "a") == True
    assert ComparisonUtils.check_if_greater("", "hello") == True
    
    # Mixed types might fail depending on Python version strictness, but we ensure basic functionality first.
    # Testing with a custom object to demonstrate encapsulation potential if extended later:
    class MyNumber(int):
        pass

    num = MyNumber(20)
    
    assert ComparisonUtils.check_if_greater(num, 15) == True
    
    print("All sample assertions passed.")