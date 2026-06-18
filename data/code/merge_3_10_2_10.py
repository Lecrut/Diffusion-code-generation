class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Prints:
            A message describing whether they are equal, if the first is greater/less than the second,
            and/or how much difference exists between them.
        """
        result = []
        
        # Check for equality with a small epsilon to handle floating-point inaccuracies
        eps = 1e-9
        if abs(temp1 - temp2) < eps:
            result.append(f"{temp1} is equal to {temp2}.")
        elif temp1 > temp2:
            diff = round(temp1 - temp2, 4)
            result.append(f"{temp1} is greater than {temp2} by {diff:.4f}.")
        else:
            diff = round(temp2 - temp1, 4)
            result.append(f"{temp1} is less than {temp2} by {diff:.4f}.")

        print(" ".join(result))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    comparator = TemperatureComparator()
    
    test_cases = [
        (25.0, 25.1),   # Slightly different positive temperatures
        (-5.5, -5.4),   # Negative temperatures close in value
        (30, 30),       # Exact integer match
        (0, 100),       # Large difference with zero reference
        (-273.15, -273.16) # Near absolute zero comparison
    ]

    for val1, val2 in test_cases:
        print(f"\nComparing {val1} and {val2}:")
        comparator.compare(val1, val2)