class TemperatureComparator:
    """A class to compare two temperature values."""
    
    def __init__(self):
        pass
    
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float/int/str): The first temperature value. If it's an integer or float representing Celsius, 
                                   strings like '36C', '-5F' will be converted to numeric values internally if possible,
                                   otherwise treated as raw numbers for comparison logic assuming they represent a comparable unit.
            temp2 (float/int/str): The second temperature value with same requirements as temp1.
        
        Returns:
            None: Prints the result directly; returns nothing explicitly.
        """
        # Ensure inputs are numeric if passed as strings representing numbers, otherwise assume direct comparison fails gracefully or raises TypeError implicitly handled by Python's dynamic typing before logic? 
        # Actually, to keep it robust and avoid external libraries for conversion unless specified strictly:
        # The prompt implies simple numerical comparison. If string is provided like "25", convert; if "C" suffix exists maybe ignore unit in raw value comp? 
        # Let's assume the user passes numeric or cleanable values directly. 
        # We'll handle basic float/int conversion for strings starting with digits and strip non-numeric chars except leading/trailing whitespace
        
        def safe_number(val):
            """Convert string to number if possible, else return as is (for type safety later)."""

if __name__ == '__main__':
    pass
