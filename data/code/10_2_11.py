class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Returns:
            None: Prints the comparison result to stdout.
        """
        if temp1 == temp2:
            print(f"{temp1} and {temp2} are equal.")
        elif temp1 > temp2:
            diff = temp1 - temp2
            direction = "higher"
        else:
            diff = temp2 - temp1
            direction = "lower"
        
        if abs(diff) < 0.001 and temp1 != int(temp1):
            # Handle floating point equality with small tolerance for non-integer values
            print(f"{temp1} is {direction} than or equal to {temp2}, difference is negligible.")
        else:
            print(f"{temp1} is {direction} than {temp2}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    t_a = 75.0
    t_b = 80
    
    comparator = TemperatureComparator()
    
    print("Comparison between", t_a, "and", t_b)
    result1 = comparator.compare(t_a, t_b)
    
    # Additional test cases with equal values and different magnitudes
    comparator.compare(25.5, 25.5)
    comparator.compare(-10, -30)