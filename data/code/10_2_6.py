class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperature values and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Returns:
            None: Prints the comparison result to standard output.
        """
        if temp1 == temp2:
            print(f"{temp1} is equal to {temp2}.")
        elif temp1 > temp2:
            diff = temp1 - temp2
            unit_str = "°C"  # Assuming Celsius for simplicity; can be extended as needed.
            if isinstance(temp1, float):
                print(f"{temp1:.2f} is {diff:.2f}{unit_str} higher than {temp2}.")
            else:
                print(f"{int(temp1)} is {int(diff)}{unit_str} higher than {int(temp2)}.")
        else:
            diff = temp2 - temp1
            unit_str = "°C"  # Assuming Celsius for simplicity.
            if isinstance(temp1, float):
                print(f"{temp1:.2f} is {diff:.2f}{unit_str} lower than {temp2}.")
            else:
                print(f"{int(temp1)} is {int(diff)}{unit_str} lower than {int(temp2)}.")

if __name__ == '__main__':
    comparator = TemperatureComparator()
    
    # Hard-coded sample values for testing without user input or external dependencies.
    temp_a = 25.0
    temp_b = 30
    
    print("Comparing temperatures:")
    comparator.compare(temp_a, temp_b)

    # Additional test cases to ensure robustness across different scenarios.
    comparator.compare(100, 98)
    comparator.compare(-5, -5)
    
    float_temp_1 = 23.45678
    int_temp_2 = 23
    
    print("\nComparing mixed types:")
    comparator.compare(float_temp_1, int_temp_2)