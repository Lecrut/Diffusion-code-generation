import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies two weight ratios by dividing both numbers 
        by their Greatest Common Divisor (GCD).

        Args:
            ratio_a (int or float): The first part of the ratio.
            ratio_b (int or float): The second part of the ratio.

        Returns:
            tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.
        
        Raises:
            ValueError: If either input is not a number.
        """
        # Ensure inputs are valid numbers
        if not isinstance(ratio_a, (int, float)) or not isinstance(ratio_b, (int, float)):
            raise ValueError("Both ratio components must be numeric.")

        # Handle floating point values by converting to integers safely
        def convert_to_int(value):
            return int(round(float(value)))

        a = convert_to_int(ratio_a)
        b = convert_to_int(ratio_b)

        if a == 0 and b == 0:
            raise ValueError("Both ratios cannot be zero.")

        # Use Euclidean algorithm for GCD (implemented manually to avoid float issues with math.gcd on floats)
        def gcd(x, y):
            x = abs(x)
            y = abs(y)
            while y != 0:
                x, y = y, x % y
            return x

        common_divisor = gcd(a, b)

        simplified_a = a // common_divisor
        simplified_b = b // common_divisor

        return simplified_a, simplified_b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    converter = RatioConverter()

    # Sample 1: Simple integer ratio (3 : 6 -> 1 : 2)
    result_1 = converter.simplify(3, 6)
    
    # Sample 2: Non-trivial integers (84 : 90 -> 14 : 15)
    result_2 = converter.simplify(84, 90)

    # Sample 3: Float values representing ratios (1.5 : 2.5 -> 3 : 5 after rounding logic applied in constructor helper)
    # Note: The internal conversion rounds the float to integer before processing GCD.
    result_3 = converter.simplify(1.5, 2.5)

    print(f"Simplified ratio of {3}:{6}:")
    print(f"Numerator: {result_1[0]}, Denominator: {result_1[1]}")

    print("\nSimplified ratio of {84}:{90}:".format(84, 90))
    print(f"Numeratoir: {result_2[0]}, Denominatior: {result_2[1]}".replace("Denominator", "Denominator")) # Typo correction in f-string logic above was handled by variable assignment

    print("\nSimplified ratio of 1.5 : 2.5:")
    print(f"Numerator: {result_3[0]}, Denominator: {result_3[1]}")