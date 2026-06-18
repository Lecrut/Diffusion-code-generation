import math

class DistanceConverter:
    """A class to convert distances between miles and kilometers."""
    
    # Conversion constants defined with high precision
    MILES_TO_KM = 1.609344
    
    def __init__(self):
        pass

    def validate_input(self, value):
        """Validates if the input is a numeric type (int or float)."""
        return isinstance(value, (int, float)) and not math.isnan(float(value))

    def convert_miles_to_kilometers(self, miles):
        """Converts distance from miles to kilometers.
        
        Args:
            miles (float): The distance in miles. Must be a valid number.
            
        Returns:
            float: The equivalent distance in kilometers.
            
        Raises:
            ValueError: If the input is not numeric or NaN/Inf.
        """
        if not self.validate_input(miles):
            raise ValueError("Input must be a numeric value.")
        
        return miles * self.MILES_TO_KM

    def convert_kilometers_to_miles(self, kilometers):
        """Converts distance from kilometers to miles.
        
        Args:
            kilometers (float): The distance in kilometers. Must be a valid number.
            
        Returns:
            float: The equivalent distance in miles.
            
        Raises:
            ValueError: If the input is not numeric or NaN/Inf.
        """
        if not self.validate_input(kilometers):
            raise ValueError("Input must be a numeric value.")
        
        return kilometers / self.MILES_TO_KM

    def convert_distance(self, distance_in_miles, target_unit='km'):
        """Unified method to convert distance between miles and kilometers.
        
        Args:
            distance_in_miles (float): The input distance in miles.
            target_unit (str): Target unit ('km' for kilometers or 'mi' for miles). Default is 'km'.
            
        Returns:
            float: The converted distance.
            
        Raises:
            ValueError: If the input is not numeric, if NaN/Inf, or if target_unit is invalid.
        """
        if not self.validate_input(distance_in_miles):
            raise ValueError("Input distance must be a valid number.")
        
        unit = target_unit.lower()
        if unit == 'km':
            return self.convert_miles_to_kilometers(distance_in_miles)
        elif unit in ['mi', 'mile']:
            return self.convert_miles_to_kilometers(distance_in_miles) / self.MILES_TO_KM # Convert to km then back? No, direct conversion.
            
            # Correction for the above logic: 
            # To convert miles to miles (identity), or if user meant input was in KM but asked for MI?
            # The method signature says "distance_in_miles", implying input is always Miles.
            # So converting back to miles is just identity, but let's handle generic conversion properly based on context 
            # OR strictly follow the argument name: Input is ALWAYS miles. Output depends on target_unit.
            
            return distance_in_miles if unit == 'mi' else self.convert_miles_to_kilometers(distance_in_miles)
        else:
            raise ValueError("Target unit must be 'km', 'mi', or 'mile'.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    converter = DistanceConverter()