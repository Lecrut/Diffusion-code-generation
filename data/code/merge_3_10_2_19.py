class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Returns:
            None: Prints the comparison result to standard output.
        """
        if temp1 == temp2:
            print(f"{temp1} is equal to {temp2}")
        elif temp1 > temp2:
            diff = round(temp1 - temp2, 4)
            print(f"{temp1} is greater than {temp2} by {diff}")
        else:
            diff = round(abs(temp1 - temp2), 4)
            print(f"{temp1} is less than {temp2} by {diff}")

if __name__ == '__main__':
    comparator = TemperatureComparator()

    # Sample test cases with hard-coded values
    sample_cases = [
        (30.5, 30.5),      # Equal case
        (45.2, -5.8),      # Greater than case
        (-10.0, 20.0),     # Less than case
        (99.9, 100.0)      # Very close values with slight difference
    ]

    for temp_a, temp_b in sample_cases:
        print(f"\nComparing {temp_a} and {temp_b}:")
        comparator.compare(temp_a, temp_b)