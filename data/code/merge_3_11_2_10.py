import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.

        Args:
            num1 (int or float): The numerator value. If not an integer, 
                                it will be converted by rounding to nearest int.
            num2 (int or float): The denominator value. If zero is passed, 
                                a ValueError is raised.

        Returns:
            tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.

        Raises:
            ZeroDivisionError: If num2 is 0.
        """
        # Ensure inputs are treated as integers to avoid floating point precision issues in division logic
        if not isinstance(num1, (int)) or type(num1) == float:
            try:
                rounded_num1 = int(round(float(num1)))
            except ValueError:
                raise TypeError("num1 must be convertible to an integer")

        if not isinstance(num2, (int)) or type(num2) == float:
            try:
                rounded_num2 = int(round(float(num2)))
            except ValueError:
                raise TypeError("num2 must be convertible to an integer")

        num1_int = rounded_num1
        num2_int = rounded_num2

        if num2_int == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        common_divisor = math.gcd(int(abs(num1)), int(abs(num2)))
        
        simplified_numerator = int(abs(num1) // common_divisor * (1 if num1 >= 0 else -1))
        simplified_denominator = int(num2_int // abs(common_divisor))
        
        # Adjust sign so the denominator remains positive, as per standard mathematical conventions for ratios
        if simplified_denominator < 0:
            return (-simplified_numerator, -simplified_denominator)

        return (simplified_num1 := simplified_numerator, 
                simplified_denominator := int(simplified_denominator))

if __name__ == '__main__':
    # Sample values for testing the RatioCalculator class
    calculator = RatioCalculator()

    test_cases = [
        84, "36",     # Int and string
        -12, 90,      # Negative number
        5.5, 2.5,     # Floats (will be rounded)
        70, "-21"    # Mixed negative signs
    ]

    for i in range(0, len(test_cases), 2):
        num1 = test_cases[i]
        num2 = test_cases[i+1] if i + 1 < len(test_cases) else "45" # Ensure a default second value
        
        try:
            numerator, denominator = calculator.simplify_ratio(num1, num2)
            print(f"Simplified ratio of {num1} to {num2}: Numerator={numerator}, Denominator={denominator}")
        except (ValueError, TypeError) as e:
            print(f"An error occurred for inputs ({num1}, {num2}): {e}")