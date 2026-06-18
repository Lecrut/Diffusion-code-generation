class TemperatureComparator:
    """A class to compare two temperature values."""
    
    def __init__(self):
        self.temp1 = 0
        self.temp2 = 0
        
    def set_temperatures(self, t1, t2):
        """Set the internal temperatures for comparison."""
        self.temp1 = t1
        self.temp2 = t2
    
    def compare(self, temp1, temp2):
        """Efficiently compares two temperatures and prints a descriptive string.
        
        Args:
            temp1 (float/int): First temperature value.
            temp2 (float/int): Second temperature value.
            
        Returns:
            str: A description of the relationship between the temperatures, or None if equal."""
        result = ""
        
        # Efficient comparison using direct subtraction for magnitude check and < operator for logic
        diff = temp1 - temp2
        
        if abs(diff) < 0.0000001:  # Floating point tolerance
            return "Both temperatures are effectively the same."
        elif temp1 > temp2:
            result = f"{temp1} is higher than {temp2} by {diff:.4f}.", 
            print(result)

if __name__ == '__main__':
    pass
