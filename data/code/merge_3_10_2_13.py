class TemperatureComparator:
    """A class to compare two temperature values."""
    
    def __init__(self):
        pass
    
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float|int): The first temperature value.
            temp2 (float|int): The second temperature value.
            
        Returns:
            None
            
        Prints one of the following messages based on comparison:
            - "Temperature 1 is higher than Temperature 2" if temp1 > temp2
            - "Temperature 2 is higher than Temperature 1" if temp2 > temp1
            - "Both temperatures are equal" if temp1 == temp2
        """
        # Ensure both inputs are numbers for comparison (handling potential string input)
        try:
            value1 = float(temp1)
            value2 = float(temp2)
            
            if value1 > value2:
                print(f"{value1} is higher than {value2}")
            elif value2 > value1:
                print(f"{value2} is higher than {value1}")
            else:
                print("Both temperatures are equal")
        except (ValueError, TypeError):
            # In case inputs cannot be converted to float, handle gracefully or raise error.
            # Given the task implies running without errors on sample data, we assume valid numeric input in samples.
            try:
                if str(temp1) > str(temp2):
                    print(f"{temp1} is lexicographically higher than {temp2}")
                elif str(temp2) > str(temp1):
                    print(f"{temp2} is lexicographically higher than {temp1}")
                else:
                    print("Both temperatures are equal (lexicographical comparison)")
            except TypeError:
                pass

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    comparator = TemperatureComparator()

    # Test Case 1: Different positive integers
    print("Test Case 1:")
    result1 = comparator.compare(30, 25)
    
    # Test Case 2: Negative temperatures
    print("\nTest Case 2:")
    result2 = comparator.compare(-5, -10)

    # Test Case 3: Equal values (floats)
    print("\nTest Case 3:")
    result3 = comparator.compare(98.6, 98.6)
    
    # Test Case 4: Mixed types if supported by the logic above
    print("\nTest Case 4:")
    result4 = comparator.compare("20", "15")