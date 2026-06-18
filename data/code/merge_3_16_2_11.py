class NumberChecker:
    """A utility class to check numerical properties."""
    
    def check_positivity(self, value):
        """
        Determines if a given numeric value is positive.
        
        A number is considered positive if it is strictly greater than zero.
        
        Args:
            value (int or float): The number to be checked.
            
        Returns:
            bool: True if the value is positive, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    samples = [10, -5, 0, 3.5, "not a number"]  # Note: string will cause TypeError in strict check
    
    try:
        for sample in samples[:4]:  # Skip the non-numeric example to avoid runtime error as per best practice demonstration logic
            result = checker.check_positivity(sample)
            print(f"Is {sample} positive? {result}")
    except (TypeError, ValueError):
        pass
        
    # Additional explicit test for edge cases if needed directly in loop without try-except on string to demonstrate correctness
    
    samples_corrected = [10.5, -3, 0]
    
    print("Testing corrected numeric samples:")
    for val in samples_corrected:
        result = checker.check_positivity(val)
        print(f"check_positivity({val}) -> {result}")