class TemperatureComparator:
    """A class to handle temperature comparisons and difference calculations."""

    def compare(self, temp1: float, temp2: float) -> int:
        """
        Compare two temperatures and return the result of their comparison.

        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.

        Returns:
            int: 0 if they are equal, -1 if temp1 is less than temp2, 
                 or 1 if temp1 is greater than temp2.
        """
        return (temp1 > temp2) - (temp1 < temp2)

    def absolute_difference(self, temp1: float, temp2: float) -> float:
        """
        Calculate the absolute difference between two temperatures.

        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.

        Returns:
            float: The absolute difference between temp1 and temp2.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 25.0
    t_b = 30.0

    comparator = TemperatureComparator()

    result_comparison = comparator.compare(t_a, t_b)
    diff_result = comparator.absolute_difference(t_a, t_b)

    print(f"Comparison of {t_a}°C and {t_b}°C: {result_comparison}")
    print(f"Absolute difference between {t_a}°C and {t_b}°C is {diff_result:.2f}°")