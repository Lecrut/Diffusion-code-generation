class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    # Conversion constants (meters)
    METER_TO_KILOMETER = 0.001
    KILOMETER_TO_MILE = 0.621371
    MILE_TO_METERS = 1609.34
    
    def __init__(self, distance: float):
        """Initialize the converter with a base distance in meters."""
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be an integer or float.")
        self.distance_meters = max(0, distance)

    def to_kilometers(self) -> float:
        """Convert distance from meters to kilometers. Returns a new DistanceConverter."""
        return DistanceConverter(self.distance_meters * self.METER_TO_KILOMETER)

    def to_miles(self) -> float:
        """Convert distance from meters to miles. Returns a new DistanceConverter."""
        return DistanceConverter(self.distance_meters / self.MILE_TO_METERS)

    @classmethod
    def convert_from(cls, value: float, unit: str) -> "DistanceConverter":
        """Create a converter instance directly from any supported unit string and value.
        
        Args:
            value (float): The numeric distance value.
            unit (str): One of 'meters', 'kilometers', or 'miles'.
            
        Returns:
            DistanceConverter: A new instance initialized with the converted meters.
            
        Raises:
            ValueError: If an invalid unit string is provided.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        
        valid_units = ['meters', 'kilometers', 'miles']
        if unit.lower() not in valid_units:
            raise ValueError(f"Unsupported unit '{unit}'. Supported units are {valid_units}.")

        # Convert input to meters first, then initialize the class
        converted_meters = value
        
        if unit.lower() == 'kilometers':
            converted_meters *= 1000.0
        elif unit.lower() == 'miles':
            converted_meters *= cls.MILE_TO_METERS
            
        return DistanceConverter(converted_meters)

if __name__ == '__main__':
    # Sample usage without user input
    
    # Test Case 1: Initialize with meters and convert to kilometers/miles
    d1 = DistanceConverter(500.0)
    print(f"Original (meters): {d1.distance_meters}")
    
    km_converter = d1.to_kilometers()
    miles_converter = d1.to_miles()
    
    print(f"In Kilometers: {km_converter.distance_meters} meters")
    print(f"In Miles: {miles_converter.distance_meters} meters")

    # Test Case 2: Create from string inputs (mixed units)
    try:
        km_input = DistanceConverter.convert_from(10, 'kilometers')
        mi_input = DistanceConverter.convert_from(5, 'miles')
        
        print(f"\nFrom input of {km_input.distance_meters} meters")
        print(f"  -> Kilometers: {km_input.to_kilometers().distance_meters}")
        print(f"  -> Miles: {km_input.to_miles().distance_meters}")

        print(f"\nFrom input of {mi_input.distance_meters} meters")
        print(f"  -> Kilometers: {mi_input.to_kilometers().distance_meters}")
        print(f"  -> Miles: {mi_input.to_miles().distance_meters}")
    except Exception as e:
        # This block is unreachable given the valid inputs, but ensures robustness
        raise

    # Test Case 3: Error handling demonstration (commented out to prevent runtime errors in execution)
    # try:
    #     DistanceConverter.convert_from(10, 'yards') 
    # except ValueError as ve:
    #     print(f"Caught expected error: {ve}")