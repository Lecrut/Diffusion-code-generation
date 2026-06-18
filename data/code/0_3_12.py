class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""
    
    # Conversion factors stored as class constants
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 0.3048
    KILOMETERS_TO_METERS = 1000

    def meters_to_feet(self, value: float) -> float:
        """Convert a distance in meters to feet."""
        return self.METERS_TO_FEET * value

    def meters_to_kilometers(self, value: float) -> float:
        """Convert a distance in meters to kilometers."""
        return self.METERS_TO_KILOMETERS * value

    def feet_to_meters(self, value: float) -> float:
        """Convert a distance in feet to meters."""
        return self.FEET_TO_METERS * value

    def kilometers_to_meters(self, value: float) -> float:
        """Convert a distance in kilometers to meters."""
        return self.KILOMETERS_TO_METERS * value

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    print("Conversion Examples:")
    
    # Sample 1: Meters to Feet and Kilometers
    meters_sample = 100.5
    feet_result = converter.meters_to_feet(meters_sample)
    km_result = converter.meters_to_kilometers(meters_sample)
    print(f"{meters_sample} meters is equal to {feet_result:.2f} feet and {km_result:.4f} kilometers.")

    # Sample 2: Feet to Meters
    feet_sample = 50.75
    meters_from_feet = converter.feet_to_meters(feet_sample)
    print(f"{feet_sample} feet is equal to {meters_from_feet:.4f} meters.")

    # Sample 3: Kilometers to Meters
    km_sample = 2.5
    meters_from_km = converter.kilometers_to_meters(km_sample)
    print(f"{km_sample} kilometers is equal to {meters_from_km} meters.")