import math

class TemperatureComparator:
    """A class to perform operations on temperature values."""

    def compare(self, temp1: float, temp2: float) -> int:
        """Compare two temperatures and return the result of their comparison.
        
        Args:
            temp1 (float): The first temperature value in Celsius.
            temp2 (float): The second temperature value in Celsius.
            
        Returns:
            int: -1 if temp1 is less than temp2, 0 if equal, and 1 if greater.
        """
        return -1 if temp1 < temp2 else (-1 if temp1 == temp2 else 1)

    def calculate_absolute_difference(self, temp1: float, temp2: float) -> float:
        """Calculate the absolute difference between two temperatures.
        
        Args:
            temp1 (float): The first temperature value in Celsius.
            temp2 (float): The second temperature value in Celsius.
            
        Returns:
            float: The absolute difference between the two temperatures, rounded to 4 decimal places for cleanliness.
        """
        return round(abs(temp1 - temp2), 4)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    t_a = 35.6789
    t_b = 20.1234

    comparator = TemperatureComparator()

    result_comparison = comparator.compare(t_a, t_b)
    diff_result = comparator.calculate_absolute_difference(t_a, t_b)

    print(f"Comparison of {t_a}°C and {t_b}°C: {'Lower' if result_comparison == -1 else 'Equal' if result_comparison == 0 else 'Higher'}")
    print(f"Absolute difference between the two temperatures: {diff_result}")