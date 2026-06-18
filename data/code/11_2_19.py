class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple: A tuple containing two integers representing the simplified ratio [a, b].
                   If inputs are not numeric or if den is zero, returns None.
        
        Raises:
            TypeError: If input types are unsupported or if num2 is non-numeric.
        """
        # Validate input types
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            try:
                n = int(round(float(num1)))
                d = int(round(float(num2)))
                
                if d == 0:
                    return None
                
                # Calculate GCD using Euclidean algorithm for integers
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return abs(a)
                
                common_divisor = gcd(n, d)
                
                simplified_num1 = n // common_divisor
                simplified_num2 = d // common_divisor
                
                # Ensure positive denominator for consistency (optional standard practice)
                if simplified_num2 < 0:
                    simplified_num1 = -simplified_num1
                    simplified_num2 = -simplified_num2
                    
                return [simplified_num1, simplified_num2]
            except (ValueError, OverflowError):
                raise TypeError("Inputs must be valid numbers.")
        else:
            raise TypeError(f"Both num1 and num2 must be numeric types. Received {type(num1).__name__} and {type(num2).__name__}.")

if __name__ == '__main__':
    # Hard-coded sample values to test the RatioCalculator class without user input
    
    calculator = RatioCalculator()
    
    # Test Case 1: Basic integers (e.g., 4/8 -> 1/2)
    result1 = calculator.simplify_ratio(4, 8)
    print(f"Ratio of {4} to {8}: {[result1[0], result1[1]]}")

    # Test Case 2: Negative numbers (e.g., -3/-9 -> 1/3)
    result2 = calculator.simplify_ratio(-3, -9)
    print(f"Ratio of {-3} to {-9}: {[result2[0], result2[1]]}")

    # Test Case 3: Different signs (e.g., 6/-4 -> -3/2)
    result3 = calculator.simplify_ratio(6, -4)
    print(f"Ratio of {6} to {-4}: {[result3[0], result3[1]]}")

    # Test Case 4: Floats that convert cleanly (e.g., 5.0/2.5 -> 2/1)
    result4 = calculator.simplify_ratio(5.0, 2.5)
    print(f"Ratio of {5.0} to {2.5}: {[result4[0], result4[1]]}")

    # Test Case 5: Edge case - zero denominator (should return None or handle gracefully based on design; here returning None as per logic above if d==0)
    try:
        result5 = calculator.simplify_ratio(5, 0)
        print(f"Ratio of {5} to {0}: {result5}")
    except Exception as e:
        # The class returns None for zero denominator based on internal check; 
        # if an exception was intended here during design phase it would be raised.
        pass

    # Test Case 6: Large numbers
    result6 = calculator.simplify_ratio(12345, 98760)
    print(f"Ratio of {12345} to {98760}: {[result6[0], result6[1]]}")

    # Test Case 7: Invalid input type (int and string mixed - expected to raise TypeError inside method logic if not caught externally, 
    # but our check raises it explicitly)
    try:
        invalid_result = calculator.simplify_ratio(5, "3")
    except TypeError as e:
        print(f"Expected error for invalid input type occurred: {e}")

    # Test Case 8: Unity ratio (1/1 -> 1/1)
    result7 = calculator.simplify_ratio(20, 20)
    print(f"Ratio of {20} to {20}: {[result7[0], result7[1]]}")