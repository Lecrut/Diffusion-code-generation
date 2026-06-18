class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""
    
    # Conversion factors stored as class constants
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET
    
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1 / METERS_TO_KILOMETERS

    def meters_to_feet(self, value: float) -> float:
        """Convert distance from meters to feet."""
        return self.METERS_TO_FEET * value

    def feet_to_meters(self, value: float) -> float:
        """Convert distance from feet to meters."""
        return self.FEET_TO_METERS * value

    def meters_to_kilometers(self, value: float) -> float:
        """Convert distance from meters to kilometers."""
        return self.METERS_TO_KILOMETERS * value

    def kilometers_to_meters(self, value: float) -> float:
        """Convert distance from kilometers to meters."""
        return self.KILOMETERS_TO_METERS * value

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    print("Conversion Results:")
    
    # Sample 1: Meters to Feet and Kilometers
    meters_val = 100.5
    feet_result = converter.meters_to_feet(meters_val)
    km_result = converter.meters_to_kilometers(meters_val)
    print(f"{meters_val} meters is {feet_result:.2f} feet and {km_result:.4f} kilometers.")

    # Sample 2: Feet to Meters
    feet_val = 50.75
    meters_from_feet = converter.feet_to_meters(feet_val)
    print(f"{feet_val} feet is {meters_from_feet:.4f} meters.")

    # Sample 3: Kilometers to Meters
    km_val = 2.5
    meters_from_km = converter.kilometers_to_meters(km_val)
    print(f"{km_val} kilometers is {meters_from_km:.4f} meters.")