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

    # Sample conversions
    meter_value = 100.5
    feet_result = converter.meters_to_feet(meter_value)
    
    km_value = 2.5
    meters_from_km = converter.kilometers_to_meters(km_value)
    
    print(f"{meter_value} m is equal to {feet_result:.4f} ft")
    print(f"{km_value} km is equal to {meters_from_km:.4f} m")