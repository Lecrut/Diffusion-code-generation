class TemperatureComparator:
    """A class to handle temperature comparisons and difference calculations."""
    
    def compare(self, temp1: float, temp2: float) -> int:
        """Compare two temperatures and return their relative order.
        
        Returns:
            0 if both are equal, -1 if temp1 is less than temp2, 
            or 1 if temp1 is greater than temp2.
        """
        if temp1 == temp2:
            return 0
        elif temp1 < temp2:
            return -1
        else:
            return 1

    def absolute_difference(self, temp1: float, temp2: float) -> float:
        """Calculate the absolute difference between two temperatures.
        
        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.
            
        Returns:
            float: The absolute difference between temp1 and temp2.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_temps = [
        (36.5, 40.0),   # Different positive temperatures
        (-5.0, -8.0),  # Both negative temperatures
        (21.0, 21.0),  # Equal temperatures
        (0.0, 100.0)   # Wide range difference
    ]

    comparator = TemperatureComparator()

    for temp_a, temp_b in sample_temps:
        comparison_result = comparator.compare(temp_a, temp_b)
        diff_result = comparator.absolute_difference(temp_a, temp_b)

        print(f"Comparing {temp_a}°C and {temp_b}°C:")
        
        if comparison_result == 0:
            status = "Equal"
        elif comparison_result < 0:
            status = f"{temp_a} is lower than {temp_b}"
        else:
            status = f"{temp_a} is higher than {temp_b}"
            
        print(f"Status: {status}")
        print(f"Absolute Difference: {diff_result:.2f}°C")
        print("-" * 40)