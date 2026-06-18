class TemperatureComparator:
    """A class to compare two temperature values."""
    
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (int or float): The first temperature value.
            temp2 (int or float): The second temperature value.
            
        Returns:
            str: A message describing the comparison result (printed to stdout instead).
        """
        if temp1 > temp2:
            print(f"{temp1} is greater than {temp2}")
        elif temp1 < temp2:
            print(f"{temp1} is less than {temp2}")
        else:
            print(f"{temp1} is equal to {temp2}")

if __name__ == '__main__':
    # Hard-coded sample values for testing
    tc = TemperatureComparator()
    
    test_cases = [
        (30, 25),
        (-5, -10),
        (22.5, 22.5),
        (0, 100)
    ]
    
    for t1, t2 in test_cases:
        result_msg = tc.compare(t1, t2)