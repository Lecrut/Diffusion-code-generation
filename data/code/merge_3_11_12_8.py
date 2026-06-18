import math

class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a: float, b: float) -> float:
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float): The numerator length.
            b (float): The denominator length.

        Returns:
            float: The calculated ratio if lengths are valid; otherwise raises ValueError.

        Raises:
            ValueError: If either or both of the provided arguments are zero, 
                      as division by zero is undefined and can cause runtime errors.
        """
        if a == 0 or b == 0:
            raise ValueError("Length cannot be zero.")
        
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()

    # Sample values for testing the get_ratio method
    length_a = 12.5
    length_b = 4.0

    try:
        ratio_result = calculator.get_ratio(length_a, length_b)
        print(f"The ratio of {length_a} to {length_b} is: {ratio_result:.2f}")
    except ValueError as e:
        print(f"Error occurred: {e}")