import math

class TemperatureComparator:
    """A class to compare two temperatures and calculate their absolute difference."""

    def __init__(self):
        pass  # No specific initialization required as input data is handled dynamically in methods

    @staticmethod
    def compare_temperatures(temp1, temp2) -> int:
        """
        Compare two temperature values.

        Returns:
            A negative number if temp1 < temp2, 
            a positive number if temp1 > temp2, 
            and zero if they are equal.
        
        Args:
            temp1 (float/int): The first temperature value.
            temp2 (float/int): The second temperature value.

        Raises:
            TypeError: If either argument is not numeric.
        """
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        
        diff = temp1 - temp2
        
        # Optimization for integer comparison to avoid floating point issues where applicable

if __name__ == '__main__':
    pass
