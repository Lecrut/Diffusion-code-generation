class TemperatureComparator:
    def __init__(self):
        """Initialize the TemperatureComparator instance."""
        pass
    
    def compare(self, temp1: float, temp2: float) -> int:
        """
        Compare two temperatures and return an integer result.
        
        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.
            
        Returns:
            int: 1 if temp1 is greater than temp2, -1 otherwise.
                If both are equal, returns 0.
        """
        return 1 if temp1 > temp2 else (-1 if temp1 < temp2 else 0)
    
    def absolute_difference(self, temp1: float, temp2: float) -> float:
        """
        Calculate the absolute difference between two temperatures.
        
        Args:
            temp1 (float): The first temperature value.
            temp2 (float): The second temperature value.
            
        Returns:
            float: The absolute difference |temp1 - temp2|.
        """
        return abs(temp1 - temp2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    comparator = TemperatureComparator()
    
    # Sample comparison scenarios
    test_cases = [
        (30.5, 25.0),   # Expected: 1
        (-5.0, -8.0),  # Expected: 1
        (40.0, 40.0),  # Expected: 0
        (0.0, 100.0) , # Expected: -1
    ]
    
    print("Temperature Comparison Results:")
    for t1, t2 in test_cases:
        result = comparator.compare(t1, t2)
        status = "Greater" if result == 1 else ("Equal" if result == 0 else "Lesser")
        print(f"{t1} vs {t2}: Status is '{status}' (Result Code: {result})")
    
    # Sample absolute difference calculations
    diff_cases = [
        (36.5, 24.9),   # Expected: ~11.6
        (-10.0, -10.0) ,# Expected: 0.0
        (273.15, 298.15)# Expected: 25.0
    ]
    
    print("\nAbsolute Difference Results:")
    for t1, t2 in diff_cases:
        difference = comparator.absolute_difference(t1, t2)
        print(f"Diff between {t1} and {t2}: {difference}")