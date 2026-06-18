class TemperatureComparator:
    """A utility class to perform temperature comparisons."""

    def compare(self, temp1: float, temp2: float) -> int:
        """
        Compares two temperatures and returns their relative order.
        
        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.
            
        Returns:
            int: 1 if temp1 > temp2, -1 if temp1 < temp2, 0 otherwise.
        """
        if temp1 == temp2:
            return 0
        elif temp1 > temp2:
            return 1
        else:
            return -1

    def absolute_difference(self, temp1: float, temp2: float) -> float:
        """
        Calculates the absolute difference between two temperatures.
        
        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.
            
        Returns:
            float: The non-negative distance between the two values.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    t_a = 23.5
    t_b = 18.0
    
    comparator = TemperatureComparator()
    
    comparison_result = comparator.compare(t_a, t_b)
    diff = comparator.absolute_difference(t_a, t_b)
    
    print(f"Comparing {t_a}°C and {t_b}°C:")
    if comparison_result == 1:
        print("First temperature is higher.")
    elif comparison_result == -1:
        print("Second temperature is higher.")
    else:
        print("Temperatures are equal.")
    
    print(f"Absolute difference between the temperatures: {diff}°C")