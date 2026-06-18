class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""

    # Conversion factors stored as class constants
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET
    METER_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METER = 1 / METER_TO_KILOMETERS

    def meters_to_feet(self, value: float) -> float:
        """Convert a distance in meters to feet."""
        return self.METERS_TO_FEET * value

    def feet_to_meters(self, value: float) -> float:
        """Convert a distance in feet to meters."""
        return self.FEET_TO_METERS * value

    def meters_to_kilometers(self, value: float) -> float:
        """Convert a distance in meters to kilometers."""
        return self.METER_TO_KILOMETERS * value

    def kilometers_to_meters(self, value: float) -> float:
        """Convert a distance in kilometers to meters."""
        return self.KILOMETERS_TO_METER * value

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    print(f"{10} meters is {converter.meters_to_feet(10):.2f} feet.")
    print(f"{50} feet is {converter.feet_to_meters(50):.4f} meters.")
    print(f"{1000} meters is {converter.meters_to_kilometers(1000):.3f} kilometers.")
    print(f"{2} kilometers is {converter.kilometers_to_meters(2):.2f} meters.")