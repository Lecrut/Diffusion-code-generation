class TemperatureComparator:
    """A class to compare temperatures and calculate differences."""

    def __init__(self, unit='celsius'):
        """Initialize with a default temperature unit of celsius.

        Args:
            unit (str): The temperature unit ('celsius' or 'fahrenheit'). Defaults to 'celsius'.
        """
        self.unit = unit.lower() if isinstance(unit, str) else 'celsius'

    def get_temperature(self, value):
        """Return the stored temperature.

        Args:
            value (float): The temperature value.

        Returns:
            float: The provided temperature value.
        """
        return value

    def compare_temperatures(self, temp1, temp2):
        """Compare two temperatures and determine which is higher or if they are equal.

        Args:
            temp1 (float): First temperature value.
            temp2 (float): Second temperature value.

        Returns:
            int: 0 if temps are equal, 1 if t1 > t2, -1 otherwise.
        """
        return 0 if temp1 == temp2 else (1 if temp1 > temp2 else -1)

    def calculate_absolute_difference(self, temp1, temp2):
        """Calculate the absolute difference between two temperatures in the same unit.

        Args:
            temp1 (float): First temperature value.
            temp2 (float): Second temperature value.

        Returns:
            float: The absolute difference between the two values.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Sample usage without user input or external dependencies
    comparator = TemperatureComparator(unit='celsius')

    t_a = 25.0
    t_b = 30.0

    comparison_result = comparator.compare_temperatures(t_a, t_b)
    difference = comparator.calculate_absolute_difference(t_a, t_b)

    print(f"Comparing {t_a}°C and {t_b}°C")
    if comparison_result == 0:
        result_msg = "Equal"
    elif comparison_result == 1:
        result_msg = f"{t_a} is higher than {t_b}"
    else:
        result_msg = f"{t_b} is higher than {t_a}"

    print(f"Result: {result_msg}")
    print(f"Absolute difference: {difference:.2f}°C")