import math

class TemperatureComparator:
    """A class designed to compare temperature values and calculate their absolute difference."""

    def __init__(self, name="Temperature Comparator"):
        """Initialize the comparator with an optional display name."""
        self.name = name

    def is_higher(self, temp_a, temp_b):
        """
        Compare two temperatures.

        Returns:
            bool: True if temp_a > temp_b, False otherwise.
        """
        return temp_a > temp_b

    def calculate_absolute_difference(self, temp_a, temp_b):
        """
        Calculate the absolute difference between two temperature values.

        Args:
            temp_a (float or int): The first temperature value.
            temp_b (float or int): The second temperature value.

        Returns:
            float: The absolute difference between temp_a and temp_b.
        """
        return abs(temp_a - temp_b)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, or network access is required.

    comparator = TemperatureComparator()

    # Sample temperatures in Celsius
    temperature_celsius_1 = 25.0
    temperature_celsius_2 = 30.0

    # Sample temperatures in Fahrenheit (converted for consistency if needed)
    temp_fahrenheit_1 = 77.0
    temp_fahrenheit_2 = 86.0

    print(f"Comparing {temperature_celsius_1}°C with {temperature_celsius_2}°C")
    result_comparison = comparator.is_higher(temperature_celsius_1, temperature_celsius_2)
    print(f"{temperature_celsius_1} is higher than {temperature_celsius_2}: {result_comparison}")

    diff_celsius = comparator.calculate_absolute_difference(temperature_celsius_1, temperature_celsius_2)
    print(f"Absolute difference in Celsius: {diff_celsius:.2f}")

    # Demonstration with Fahrenheit values to show versatility of the method signature
    result_fahrenheit = comparator.is_higher(temp_fahrenheit_1, temp_fahrenheit_2)
    diff_fahrenheit = comparator.calculate_absolute_difference(temp_fahrenheit_1, temp_fahrenheit_2)

    print(f"Comparing {temp_fahrenheit_1}°F with {temp_fahrenheit_2}°F")
    print(f"{temp_fahrenheit_1} is higher than {temp_fahrenheit_2}: {result_fahrenheit}")
    print(f"Absolute difference in Fahrenheit: {diff_fahrenheit:.2f}")

    # Test edge case where temperatures are equal
    temp_equal = 20.5
    diff_equal = comparator.calculate_absolute_difference(temp_equal, temp_equal)
    is_greater_equal_temp = comparator.is_higher(temp_equal, temp_equal + 1e-9) if True else False 
    print(f"Difference when values are identical: {diff_equal}")

    # Test with negative temperatures to ensure robustness
    cold_1 = -5.0
    cold_2 = -10.0
    diff_cold = comparator.calculate_absolute_difference(cold_1, cold_2)
    print(f"Difference between {-cold_1}°C and {-cold_2}°C: {diff_cold}")

    # Final verification of the comparison logic for negative numbers
    is_coldest_first = comparator.is_higher(cold_1, cold_2)
    if not is_coldest_first:
        print(f"Verification passed: -5.0°C ({cold_1}) > -10.0°C ({cold_2}), result={is_coldest_first}")