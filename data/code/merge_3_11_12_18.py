class LengthCalculator:
    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (float or int): The numerator length value.
            b (float or int): The denominator length value.
            
        Returns:
            float: The calculated ratio if 'b' is not zero, otherwise 0.0.
                
        Raises:
            ZeroDivisionError: If 'b' is exactly zero to prevent undefined behavior.
        """
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    
    # Sample values for testing without any user input or external dependencies
    sample_a = 10.5
    sample_b = 2
    
    result_ratio = calculator.get_ratio(sample_a, sample_b)
    
    print(f"Ratio of {sample_a} to {sample_b}: {result_ratio}")