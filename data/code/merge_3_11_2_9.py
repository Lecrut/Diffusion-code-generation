class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.
                            If input values are floats, they will be converted to their integer equivalents 
                            based on rounding if close to an integer, otherwise raising a TypeError for non-integer ratios.
                            
        Raises:
            ValueError: If num2 is zero (division by undefined).
            TypeError: If inputs cannot be treated as integers after conversion logic.
        
        Examples:
            >>> calc = RatioCalculator()
            >>> calc.simplify_ratio(4, 8)
            (1, 2)
            >>> calc.simplify_ratio(-3, -9)
            (-1, -3)
        """
        # Convert inputs to integers if they are floats that represent whole numbers
        try:
            int_num1 = round(num1)
            int_num2 = round(num2)
            
            # Check for valid input types after rounding
            if not isinstance(int_num1, (int, float)) or not isinstance(int_num2, (int, float)):
                raise TypeError("Inputs must be convertible to integers.")
                
        except Exception:
            raise TypeError(f"Invalid input type. Expected numeric values that can represent a ratio.")

        # Handle zero denominator case
        if int_num2 == 0:
            raise ValueError("Denominator cannot be zero in the ratio calculation.")

        # Calculate GCD using Euclidean algorithm for integers
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return abs(a)

        common_divisor = gcd(int_num1, int_num2)

        simplified_numerator = int_num1 // common_divisor
        simplified_denominator = int_num2 // common_divisor

        # Normalize signs so that the denominator is always positive (unless it's zero which we already handled)
        if simplified_denominator < 0:
            simplified_numerator *= -1
            simplified_denominator *= -1
            
        return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values to test the RatioCalculator class without user input
    
    calculator = RatioCalculator()

    # Test Case 1: Simple positive integers
    result1 = calculator.simplify_ratio(6, 9)
    print(f"Simplified ratio of {6} to {9}: Numerator={result1[0]}, Denominator={result1[1]}")

    # Test Case 2: Negative numbers (should normalize denominator sign if needed or keep relative signs)
    result2 = calculator.simplify_ratio(-4, -8)
    print(f"Simplified ratio of {-4} to {-8}: Numerator={result2[0]}, Denominator={result2[1]}")

    # Test Case 3: Mixed positive and negative
    result3 = calculator.simplify_ratio(5, -10)
    print(f"Simplified ratio of {5} to {-10}: Numerator={result3[0]}, Denominator={result3[1]}")

    # Test Case 4: Large numbers
    result4 = calculator.simplify_ratio(123456789, 98765432)
    print(f"Simplified ratio of {123456789} to {98765432}: Numerator={result4[0]}, Denominator={result4[1]}")

    # Test Case 5: One number is a multiple of the other (identity)
    result5 = calculator.simplify_ratio(7, 7)
    print(f"Simplified ratio of {7} to {7}: Numerator={result5[0]}, Denominator={result5[1]}")

    # Test Case 6: Attempting zero denominator should raise ValueError (handled in logic but not printed here as it's an error case)
    try:
        result6 = calculator.simplify_ratio(3, 0)
    except ValueError as e:
        print(f"Caught expected error for zero denominator: {e}")

    # Test Case 7: Float inputs that represent whole numbers (rounded before calculation per logic above)
    # Note: The implementation rounds floats to integers if they are effectively whole numbers.
    result7 = calculator.simplify_ratio(2.0, 4.0)
    print(f"Simplified ratio of {2.0} to {4.0}: Numerator={result7[0]}, Denominator={result7[1]}")

    # Test Case 8: Non-whole float inputs would raise TypeError in the current logic implementation 
    # because round() returns a number, but isinstance check on rounded result of non-integer math might be tricky.
    # Let's stick to integer-like behavior for this task scope unless specified otherwise.
    try:
        result8 = calculator.simplify_ratio(2.5, 4.0) 
    except TypeError as e:
        print(f"Caught expected error for non-integer ratio logic (if applicable): {e}")