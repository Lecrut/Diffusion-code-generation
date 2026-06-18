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
            print(f"{temp1} is equal to {temp2}")
        elif temp1 > temp2:
            diff = temp1 - temp2
            print(f"{temp1} is greater than {temp2} by {diff:.2f}")
        else:
            diff = temp2 - temp1
            print(f"{temp1} is less than {temp2} by {diff:.2f}")

if __name__ == '__main__':
    comparator = TemperatureComparator()
    
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 36.5
    t_b = 72
    
    print("Comparing temperatures:")
    result1 = "Result:"
    comparator.compare(t_a, t_b)