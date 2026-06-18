import math

class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""
    
    # Constants defining conversion rates relative to 1 meter
    METERS_PER_KILOMETER = 0.001
    MILES_PER_METER = 6.2137e-4
    
    def __init__(self):
        """Initialize the DistanceConverter with default constants."""
        pass

    def convert_to_meters(self, value: float) -> float:
        """Convert any distance to meters.
        
        Args:
            value (float): The distance in kilometers or miles.
            
        Returns:
            float: The equivalent distance in meters.
        """
        if isinstance(value, str):
            # Handle string inputs by attempting conversion first as a fallback for robustness
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Input must be a number or convertible to float.")
            
            return self._convert_to_meters(numeric_value)

    def _convert_to_meters(self, value: float) -> float:
        """Internal helper method to convert any distance unit to meters.
        
        Args:
            value (float): The distance in kilometers or miles.
            
        Returns:
            float: The equivalent distance in meters.
        """
        if isinstance(value, str):
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Input must be a number.")

        return value * self.METERS_PER_KILOMETER + (value * 1000 * self.MILES_PER_METER)

    def convert_to_kilometers(self, meters: float) -> float:
        """Convert distance from meters to kilometers.
        
        Args:
            meters (float): The distance in meters.
            
        Returns:
            float: The equivalent distance in kilometers.
        """
        return meters * self.METERS_PER_KILOMETER

    def convert_to_miles(self, value: float) -> float:
        """Convert any distance to miles.
        
        Args:
            value (float): The distance in meters or kilometers.
            
        Returns:
            float: The equivalent distance in miles.
        """
        if isinstance(value, str):
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Input must be a number.")

        return value * self.METERS_PER_KILOMETER + (value * 1000 * self.MILES_PER_METER)

    def convert_to_miles(self, meters: float) -> float:
        """Convert distance from meters to miles.
        
        Args:
            meters (float): The distance in meters.
            
        Returns:
            float: The equivalent distance in miles.
        """
        return meters * self.MILES_PER_METER

    def convert_to_miles(self, kilometers: float) -> float:
        """Convert distance from kilometers to miles.
        
        Args:
            kilometers (float): The distance in kilometers.
            
        Returns:
            float: The equivalent distance in miles.
        """
        return kilometers * 0.62137

    def convert_to_miles(self, meters: float) -> float:
        """Convert distance from meters to miles."""
        return meters * self.MILES_PER_METER

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = DistanceConverter()

    # Sample 1: Convert kilometers to meters and back
    km_value = 5.0
    meters_result_1 = converter.convert_to_meters(km_value)
    print(f"{km_value} kilometers is {meters_result_1:.2f} meters.")
    
    # Sample 2: Convert miles to kilometers and back
    mi_value = 3.0
    km_result_2 = converter.convert_to_kilometers(miles=mi_value * 1609.34) 
    print(f"{mi_value} miles is {km_result_2:.2f} kilometers.")

    # Sample 3: Direct conversion from meters to other units
    m_base = 1500.0
    
    km_from_meters = converter.convert_to_kilometers(m_base)
    mi_from_meters = converter.convert_to_miles(m_base)
    
    print(f"{m_base} meters is {km_from_meters:.4f} kilometers.")
    print(f"{m_base} meters is {mi_from_meters:.6f} miles.")

    # Sample 4: String input handling (if applicable in future extensions, currently handled via internal logic)
    try:
        string_input = "10"
        result_string = converter.convert_to_meters(string_input)
        print(f"{string_input} converted to meters is {result_string:.2f}")
    except Exception as e:
        # In a real scenario, we might want more specific error handling here. 
        # For this task, the logic ensures numeric conversion attempts are made first.
        pass

    # Sample 5: Mixed unit calculation simulation (Miles -> Meters)
    miles_input = 2.0
    meters_from_miles = converter.convert_to_miles(miles_input * 1609.34) 
    print(f"{miles_input} miles is {meters_from_miles:.2f} meters.")