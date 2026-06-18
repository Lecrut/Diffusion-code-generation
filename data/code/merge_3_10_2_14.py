import math

class TemperatureComparator:
    """A class to compare two temperature values."""
    
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): The first temperature value.
            temp2 (float or int): The second temperature value.
            
        Prints to stdout the comparison result as follows:
        - "Temperature {val} is higher than {temp}" if equal values are used in comparisons above.
        """
        
        if math.isinf(temp1) and math.isnan(temp1):
            print(f"Ill-defined input (NaN).")

            return

if __name__ == '__main__':
    pass
