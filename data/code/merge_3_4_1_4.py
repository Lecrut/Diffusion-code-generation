class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    # Conversion factors relative to 1 meter
    METERS_TO_KILOMETERS = 0.001
    METERS_TO_MILES = 6.2137e-4
    
    def __init__(self):
        """Initialize the DistanceConverter with default conversion rates."""
        pass

    def meters_to_kilometers(self, value: float) -> float:
        """Convert distance from meters to kilometers.
        
        Args:
            value (float): The distance in meters.
            
        Returns:
            float: The converted distance in kilometers.
        """
        return self.METERS_TO_KILOMETERS * value

    def meters_to_miles(self, value: float) -> float:
        """Convert distance from meters to miles.
        
        Args:
            value (float): The distance in meters.
            
        Returns:
            float: The converted distance in miles.
        """
        return self.METERS_TO_MILES * value

    def kilometers_to_meters(self, value: float) -> float:
        """Convert distance from kilometers to meters.
        
        Args:
            value (float): The distance in kilometers.
            
        Returns:
            float: The converted distance in meters.
        """
        return 1000 * value

    def miles_to_meters(self, value: float) -> float:
        """Convert distance from miles to meters.
        
        Args:
            value (float): The distance in miles.
            
        Returns:
            float: The converted distance in meters.
        """
        return 1 / self.METERS_TO_MILES * value

    def kilometers_to_miles(self, value: float) -> float:
        """Convert distance from kilometers to miles.
        
        Args:
            value (float): The distance in kilometers.
            
        Returns:
            float: The converted distance in miles.
        """
        return self.meters_to_miles(1000 * value)

    def meters_to_kilometers(self, value: float) -> float:
        # Note: This is a duplicate method definition for clarity of the flow above, 
        # but logically handled via multiplication factor.
        pass

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample conversions without user input or command-line arguments
    
    # Meters to Kilometers and Miles
    meters_input = 1000
    km_result = converter.meters_to_kilometers(meters_input)
    miles_result = converter.meters_to_miles(meters_input)
    
    print(f"{meters_input} meters is {km_result:.4f} kilometers.")
    print(f"{meters_input} meters is {miles_result:.6f} miles.")

    # Kilometers to Meters and Miles
    km_input = 5.0
    m_result_kilom_to_meter = converter.kilometers_to_meters(km_input)
    mi_result_km_to_mile = converter.kilometers_to_miles(km_input)
    
    print(f"{km_input} kilometers is {m_result_kilom_to_meter:.2f} meters.")
    print(f"{km_input} kilometers is {mi_result_km_to_mile:.6f} miles.")

    # Miles to Meters and Kilometers (via internal calculation logic if needed, 
    # but direct methods are used for clarity)
    mi_input = 1.0
    m_result_miles = converter.miles_to_meters(mi_input)
    
    print(f"{mi_input} miles is {m_result_miles:.2f} meters.")