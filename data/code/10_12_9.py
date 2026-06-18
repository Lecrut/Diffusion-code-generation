"""
Module to compare temperatures and calculate absolute differences.
Implements a TemperatureComparator class following best-practice OOP principles,
including encapsulation (read-only attributes), immutability design where applicable,
and single responsibility principle via dedicated methods for comparison and calculation.
"""

class TemperatureComparator:
    """
    A utility class to perform comparisons and calculations on temperature values.

    This class provides read-only access to two temperature objects and methods
    to determine which is higher/lower or equal, as well as the absolute difference
    between them. It encapsulates state within instance attributes for security 
    and consistency.
    
    Attributes:
        temp_a (float): The first numerical temperature value.
        temp_b (float): The second numerical temperature value.

    Methods:
        is_greater_than(other_temp) -> bool: Checks if self.temp_a > other_temp.
        is_less_than_or_equal_to(other_temp) -> bool: Checks if self.temp_a <= other_temp.
        calculate_absolute_difference() -> float: Returns the absolute difference between temps.
    """

    def __init__(self, temp_a: float, temp_b: float):
        """
        Initialize the TemperatureComparator with two temperature values.

        Args:
            temp_a (float): First temperature value.
            temp_b (float): Second temperature value.
        """
        self._temp_a = temp_a
        self._temp_b = temp_b

    def is_greater_than(self, other_temp: float) -> bool:
        """
        Determine if the first stored temperature is greater than a given reference temperature.

        Args:
            other_temp (float): The temperature to compare against.

        Returns:
            bool: True if self._temp_a > other_temp, False otherwise.
        """
        return self._temp_a > other_temp

    def is_less_than_or_equal_to(self, other_temp: float) -> bool:
        """
        Determine if the first stored temperature is less than or equal to a given reference temperature.

        Args:
            other_temp (float): The temperature to compare against.

        Returns:
            bool: True if self._temp_a <= other_temp, False otherwise.
        """
        return self._temp_a <= other_temp

    def calculate_absolute_difference(self) -> float:
        """
        Calculate the absolute difference between the two stored temperatures.

        Uses a private attribute for internal consistency and ensures 
        encapsulation by preventing direct modification of temperature values via getters/setters,
        maintaining object integrity as per best practices.

        Returns:
            float: The non-negative value representing |temp_a - temp_b|.
        """
        return abs(self._temp_a - self._temp_b)

if __name__ == '__main__':
    # Sample test values for TemperatureComparator functionality
    
    t_comp = TemperatureComparator(temp_a=25.5, temp_b=30.0)

    print(f"Temperature A: {t_comp._temp_a}, Temperature B: {t_comp._temp_b}")

    if t_comp.is_greater_than(31):
        print("First temperature is greater than 31°C.")
    else:
        print(f"First temperature ({t_comp._temp_a}) is not greater than 31°C.")

    comparison_result = "B is higher or equal to A" if t_comp.is_less_than_or_equal_to(25.6) \
                       else ("A and B are both below/reflection of different values") 
    
    # Note: The condition above is just illustrative logic for demonstration purposes based on hardcoded inputs
    actual_comparison_logic = "T_A <= T_B" if t_comp.is_less_than_or_equal_to(t_comp._temp_b) \
                             else ("T_A > T_B but we compare against other_temp here")

    # Direct comparison to self attributes as per method signature usage in isolation context:
    print(f"Temperature A ({t_comp._temp_a}) is less than or equal to Temperature B ({t_comp._temp_b}): {t_comp.is_less_than_or_equal_to(t_comp._temp_b)}")

    
    diff = t_comp.calculate_absolute_difference()
    if diff == 4.5:
        print(f"Absolute difference between temperatures is exactly 4.5°C.")
    else:
        print(f"Calculated absolute difference: {diff}°C (Expected: 4.5)")