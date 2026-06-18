import math

class RatioCalculator:
    """A utility class to compute ratios in their lowest terms."""

    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 and returns it as a tuple (a, b)
        representing the fraction a/b in its simplest form.

        Args:
            num1 (int or float): The numerator part of the initial ratio.
            num2 (int or float): The denominator part of the initial ratio.

        Returns:
            tuple[int, int]: A tuple containing two integers where gcd(a, b) == 1.
                             If input numbers are floats, they will be converted to ints after rounding.
        """
        # Handle zero cases explicitly for robustness before GCD logic
        if num2 == 0:
            raise ValueError("Denominator cannot be zero.")

        # Convert inputs to integers (assuming exact values as per typical ratio problems)
        a = int(round(num1))
        b = int(round(num2))

        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must represent integer-valued ratios after conversion.")

        # Calculate the Greatest Common Divisor (GCD) of absolute values to handle negatives correctly
        common_divisor = math.gcd(abs(a), abs(b))

        simplified_num1 = a // common_divisor
        simplified_num2 = b // common_divisor

        return simplified_num1, simplified_num2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    calculator = RatioCalculator()

    test_cases = [
        (4, 6),       # Expected: (2, 3)
        (-8, -12),    # Expected: (-2, -3) -> simplified usually keeps sign with numerator but here math.gcd handles magnitude
        (9, 0),       # Should raise an error or handle gracefully based on requirement; currently raises ValueError as per logic above
        (5.5, 3.3),   # Testing float handling: becomes int(6) and int(3)? Or strict integer input? 
                     # Per task "num1 to num2", usually implies integers, but rounding is safer for generic ratio calc.
    ]

    print("Running Ratio Calculator Tests...\n")

    try:
        result = calculator.simplify_ratio(4, 6)
        print(f"Ratio of {4} to {6}: Resulting in simplified form ({result[0]}, {result[1]})")

        # Test with negative numbers
        res_neg = calculator.simplify_ratio(-8, -12)
        print(f"Ratio of {-8} to {-12}: Simplified as {res_neg}")

    except ValueError as ve:
        print(f"Error encountered (as expected for invalid input): {ve}")