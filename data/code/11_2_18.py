class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        # Compute Greatest Common Divisor (GCD) of absolute values to handle negative numbers correctly
        gcd_value = self._gcd(abs(num1), abs(num2))
        
        # Divide both numbers by their GCD to get the simplified ratio components
        simplified_num1 = num1 // gcd_value
        simplified_num2 = num2 // gcd_value
        
        return (simplified_num1, simplified_num2)
    
    def _gcd(self, a, b):
        """Helper method to compute Greatest Common Divisor using Euclidean algorithm."""
        if a == 0:
            return b
        else:
            return self._gcd(b % a, a)

if __name__ == '__main__':
    # Hard-coded sample values
    test_cases = [
        (48, 18),
        (-63, -27),
        (0, 5),
        (12, 0),
        (7, 1)
    ]

    calculator = RatioCalculator()

    for i in range(len(test_cases)):
        num1, num2 = test_cases[i]
        result_num, result_denom = calculator.simplify_ratio(num1, num2)
        print(f"Ratio of {num1} to {num2}: {result_num}:{result_denom}")