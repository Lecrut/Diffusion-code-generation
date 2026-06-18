class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperature values and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): The first temperature value.
            temp2 (float or int): The second temperature value.
            
        Prints:
            A message describing whether the temperatures are equal, if one is greater than the other, 
            and which unit they share implicitly by treating them as comparable numerical values.
        """
        result = ""
        
        # Determine relationship based on numeric comparison
        if temp1 == temp2:
            result = f"The temperatures are {temp1}°C and {temp2}°C."
        elif temp1 > temp2:
            difference = temp1 - temp2
            result = f"{temp1} is greater than {temp2} by a margin of {difference} degrees."
        else:
            difference = temp2 - temp1
            result = f"{temp2} is greater than {temp1} by a margin of {difference} degrees."
        
        print(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing the TemperatureComparator class
    
    comparator = TemperatureComparator()
    
    # Test Case 1: Equal temperatures
    comparator.compare(25.5, 25.5)
    
    # Test Case 2: First temperature is higher
    comparator.compare(30.0, -5.0)
    
    # Test Case 3: Second temperature is higher
    comparator.compare(-10.0, 40.0)