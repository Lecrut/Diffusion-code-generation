class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (strictly greater than zero).
        
        Args:
            value: A numeric type to be checked.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without external input or files
    test_values = [10, -5, 0, 3.14, float('-inf'), None]
    
    results = []
    for val in test_values:
        try:
            is_positive = checker.check_positivity(val)
            # Handle non-numeric types gracefully by attempting conversion or skipping logic if needed,
            # but since the method expects numeric comparison, we'll let it raise TypeError for None to demonstrate strict behavior.
            results.append((val, is_positive))
        except (TypeError, ValueError):
            results.append(f"Error: {type(val).__name__} cannot be checked directly")

    print("NumberChecker Test Results:")
    for val, res in results:
        if isinstance(res, bool):
            status = "Positive" if res else "Non-positive"
            print(f"Value ({val}): {status}")
        else:
            print(f"Value: Error handling triggered")