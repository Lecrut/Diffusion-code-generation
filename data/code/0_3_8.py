class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""
    
    # Conversion factors stored as class constants
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET
    
    KILOMETERS_TO_METERS = 1000
    METER_TO_KILOMETERS = 1 / KILOMETERS_TO_METERS

    def meters_to_feet(self, value: float) -> float:
        """Convert distance from meters to feet."""
        return self.METERS_TO_FEET * value
    
    def feet_to_meters(self, value: float) -> float:
        """Convert distance from feet to meters."""
        return self.FEET_TO_METERS * value
    
    def kilometers_to_meters(self, value: float) -> float:
        """Convert distance from kilometers to meters."""
        return self.KILOMETERS_TO_METERS * value
    
    def meters_to_kilometers(self, value: float) -> float:
        """Convert distance from meters to kilometers."""
        return self.METER_TO_KILOMETERS * value

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    print("Sample Conversions:")
    
    # Meters to Feet
    meters_input = 10.5
    feet_output = converter.meters_to_feet(meters_input)
    print(f"{meters_input} meters is equal to {feet_output:.2f} feet")

    # Feet to Meters
    feet_input = 34.876
    meters_output = converter.feet_to_meters(feet_input)
    print(f"{feet_input} feet is equal to {meters_output:.5f} meters")

    # Kilometers to Meters
    km_input = 2.5
    meters_from_km = converter.kilometers_to_meters(km_input)
    print(f"{km_input} kilometers is equal to {meters_from_km} meters")

    # Meters to Kilometers
    meters_for_kilo = 10000
    km_output = converter.meters_to_kilometers(meters_for_kilo)
    print(f"{meters_for_kilo} meters is equal to {km_output:.2f} kilometers")