class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""

    # Conversion factors stored as class constants
    METERS_PER_KM = 1000
    FEET_PER_METER = 3.28084
    MILES_PER_FOOT = 0.000621371

    def meters_to_kilometers(self, value: float) -> float:
        """Converts a length in meters to kilometers."""
        return value / self.METERS_PER_KM

    def meters_to_feet(self, value: float) -> float:
        """Converts a length in meters to feet."""
        return value * self.FEET_PER_METER

    def kilometers_to_meters(self, value: float) -> float:
        """Converts a length in kilometers to meters."""
        return value * self.METERS_PER_KM

    def kilometers_to_feet(self, value: float) -> float:
        """Converts a length in kilometers to feet."""
        return (value * self.METERS_PER_KM) * self.FEET_PER_METER

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    print("Conversion from Meters:")
    meters_value = 100.5
    km_result = converter.meters_to_kilometers(meters_value)
    ft_result = converter.meters_to_feet(meters_value)
    print(f"{meters_value} meters is {km_result:.4f} kilometers")
    print(f"{meters_value} meters is {ft_result:.2f} feet")

    # Sample conversion from Kilometers (using different input value for variety)
    km_input = 5.0
    mt_result = converter.kilometers_to_meters(km_input)
    ft_from_km = converter.kilometers_to_feet(km_input)
    print(f"\nConversion to Meters and Feet from {km_input} kilometers:")
    print(f"{mt_result:.2f} meters")
    print(f"{ft_from_km:.4f} feet")