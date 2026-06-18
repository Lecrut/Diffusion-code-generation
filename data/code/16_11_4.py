class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the provided value is positive (strictly greater than zero).
        
        Args:
            value: The number to check.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [5, -3, 0.1, 0, float('inf'), float('-inf')]
    
    results = []
    for val in test_values:
        is_positive = checker.check_positivity(val)
        results.append(f"Value {val}: {'positive' if is_positive else 'not positive'}")
    
    print("Test Results:")
    for result in results:
        print(result)