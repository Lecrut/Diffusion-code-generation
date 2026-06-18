class TemperatureComparator:
    """A class to handle temperature comparisons and difference calculations."""

    def compare(self, temp1: float, temp2: float) -> int:
        """
        Compare two temperatures.

        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.

        Returns:
            int: 1 if temp1 is greater than temp2, -1 if less, and 0 otherwise.
        """
        diff = temp1 - temp2
        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        else:
            return 0

    def calculate_absolute_difference(self, temp1: float, temp2: float) -> float:
        """
        Calculate the absolute difference between two temperatures.

        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.

        Returns:
            float: The absolute difference between the two values.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_temp_1 = 365.47890482507
    test_temp_2 = 8

    comparator = TemperatureComparator()
    
    comparison_result = comparator.compare(test_temp_1, test_temp_2)
    difference = comparator.calculate_absolute_difference(test_temp_1, test_temp_2)

    print(f"Comparison result: {comparison_result}")
    print(f"Absolute difference: {difference}")