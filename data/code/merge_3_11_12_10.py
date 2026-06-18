class LengthCalculator:
    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.
        
        Parameters:
            a (float or int): The numerator length value.
            b (float or int): The denominator length value. Cannot be zero.
            
        Returns:
            float: The calculated ratio a/b.
            
        Raises:
            ZeroDivisionError: If 'b' is zero, which would cause division by zero error.
        
        Examples:
            >>> calc = LengthCalculator()
            >>> calc.get_ratio(10, 2)
            5.0
            
            >>> calc.get_ratio(-4, 8)
            -0.5
        
        Notes:
            This method performs a simple division operation and is designed to be efficient.
            Input validation handles the case where 'b' is zero by raising an appropriate exception.
        """
        if b == 0:
            raise ZeroDivisionError("Denominator (length 'b') cannot be zero.")
        
        return float(a) / float(b)

if __name__ == '__main__':
    # Sample usage block with hard-coded values to demonstrate functionality without user input.
    
    calculator = LengthCalculator()
    
    # Test case 1: Simple positive ratio
    sample_a_1, sample_b_1 = 20, 5
    ratio_result_1 = calculator.get_ratio(sample_a_1, sample_b_1)
    print(f"Ratio of {sample_a_1} to {sample_b_1}: {ratio_result_1}")

    # Test case 2: Negative result
    sample_a_2, sample_b_2 = -6, 3
    ratio_result_2 = calculator.get_ratio(sample_a_2, sample_b_2)
    print(f"Ratio of {sample_a_2} to {sample_b_2}: {ratio_result_2}")

    # Test case 3: Floating point lengths (simulated via integers converted internally)
    sample_a_3 = 7.5 * 100  # Effectively simulating a float input by using scaled int if needed, 
                            # but here we assume floats can be passed directly in real usage.
    # For this standalone run without external dependencies ensuring exact float type handling:
    sample_a_3 = 9 / 2       # Explicitly creates the float value 4.5
    sample_b_3 = 10         # Value for b
    
    ratio_result_3 = calculator.get_ratio(sample_a_3, sample_b_3)
    print(f"Ratio of {sample_a_3} to {sample_b_3}: {ratio_result_3}")

    # Demonstration that division by zero is handled correctly (prints error message instead of crashing uncaught if run in debugger context usually)
    try:
        sample_c = 10
        sample_d = 0
        ratio_error_test = calculator.get_ratio(sample_c, sample_d)
    except ZeroDivisionError as e:
        print(f"Handled division by zero gracefully. Error message: {e}")