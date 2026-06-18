class TemperatureComparator:
    """A class to compare temperatures and calculate their absolute difference."""

    def __init__(self, unit='celsius'):
        """Initialize with a temperature unit (optional)."""
        self.unit = unit.lower() if unit else 'celsius'

    def _convert_to_celsius(self, temp):
        """Convert any given temperature to Celsius for consistent comparison."""
        if isinstance(temp, float) or isinstance(temp, int):
            return temp
        elif hasattr(temp, '__float__'):
            try:
                val = float(temp)
                if self.unit == 'fahrenheit':
                    return (val - 32) * 5 / 9
                else:
                    return val
            except ValueError:
                raise TypeError("Temperature must be a numeric value.")

    def compare(self, temp1, temp2):
        """Compare two temperatures and return the relationship."""
        celsius_1 = self._convert_to_celsius(temp1)
        celsius_2 = self._convert_to_celsius(temp2)

        if celsius_1 > celsius_2:
            result = "Temperature 1 is higher."
        elif celsius_1 < celsius_2:
            result = "Temperature 2 is higher."
        else:
            result = "Temperatures are equal."
        
        return result

    def calculate_absolute_difference(self, temp1, temp2):
        """Calculate the absolute difference between two temperatures in Celsius."""
        celsius_1 = self._convert_to_celsius(temp1)
        celsius_2 = self._convert_to_celsius(temp2)
        abs_diff = abs(celsius_1 - celsius_2)
        
        # Convert back to original unit for display if needed, but return in Celsius as per standard practice unless specified otherwise. 
        # Here we return the difference in Celsius since it's a standardized metric.
        return abs_diff

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    
    comparator = TemperatureComparator()

    # Sample 1: Compare two Fahrenheit temperatures and calculate difference
    temp_a_fahrenheit = 98.6
    temp_b_fahrenheit = 104.0
    comparison_result_1 = comparator.compare(temp_a_fahrenheit, temp_b_fahrenheit)
    diff_1 = comparator.calculate_absolute_difference(temp_a_fahrenheit, temp_b_fahrenheit)

    # Sample 2: Compare Celsius temperatures directly
    temp_celsius_1 = 37.5
    temp_celsius_2 = 40.0
    comparison_result_2 = comparator.compare(temp_celsius_1, temp_celsius_2)
    diff_2 = comparator.calculate_absolute_difference(temp_celsius_1, temp_celsius_2)

    # Sample 3: Equal temperatures
    equal_temp = 25
    comparison_equal = comparator.compare(equal_temp, equal_temp)
    
    print(f"Comparison (Fahrenheit): {comparison_result_1}")
    print(f"Difference (Celsius): {diff_1:.2f} °C")

    print(f"\nComparison (Celsius): {comparison_result_2}")
    print(f"Difference (Celsius): {diff_2:.2f} °C")

    print("\nEqual Temperatures:")
    print(comparison_equal)