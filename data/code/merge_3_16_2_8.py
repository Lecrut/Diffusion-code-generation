class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if a given numeric value is positive.
        
        Args:
            value (int or float): The number to evaluate.
            
        Returns:
            bool: True if the value is strictly greater than zero, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    test_values = [5, -3, 0, 2.718, -0.001]
    
    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Value: {val} -> Is Positive: {result}")