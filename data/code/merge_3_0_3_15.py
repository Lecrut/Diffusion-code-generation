class UnitConverter:
    METERS_TO_FEET_FACTOR = 3.28084
    FEET_TO_METERS_FACTOR = 1 / METERS_TO_FEET_FACTOR
    
    KILOMETERS_TO_METERS_FACTOR = 1000
    METERS_TO_KILOMETERS_FACTOR = 1 / KILOMETERS_TO_METERS_FACTOR

    def meters_to_feet(self, distance_meters: float) -> float:
        """Converts a distance from meters to feet."""
        return self.METERS_TO_FEET_FACTOR * distance_meters

    def feet_to_meters(self, distance_feet: float) -> float:
        """Converts a distance from feet to meters."""
        return self.FEET_TO_METERS_FACTOR * distance_feet

    def kilometers_to_meters(self, distance_kilometers: float) -> float:
        """Converts a distance from kilometers to meters."""
        return self.KILOMETERS_TO_METERS_FACTOR * distance_kilometers

    def meters_to_kilometers(self, distance_meters: float) -> float:
        """Converts a distance from meters to kilometers."""
        return self.METERS_TO_KILOMETERS_FACTOR * distance_meters

if __name__ == '__main__':
    converter = UnitConverter()
    
    # Sample conversions using hard-coded values
    sample_meters = 100.5
    
    feet_value = converter.meters_to_feet(sample_meters)
    kilometers_value = converter.meters_to_kilometers(sample_meters)

    print(f"{sample_meters} meters is equal to {feet_value:.2f} feet.")
    print(f"{sample_meters} meters is equal to {kilometers_value:.4f} kilometers.")