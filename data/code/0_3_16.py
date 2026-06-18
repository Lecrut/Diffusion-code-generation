class UnitConverter:
    # Conversion factors to meters (1 unit = factor * meter)
    METERS_PER_METER = 1
    FEET_PER_METER = 0.3048
    KILOMETERS_PER_METER = 0.001
    
    MetersPerFoot = 1 / FEET_PER_METER
    KilometersPerMeter = KILOMETERS_PER_METER

    def meters_to_feet(self, value: float) -> float:
        """Convert distance from meters to feet."""
        return self.METERS_PER_METER * value * self.FEET_PER_METER
    
    def meters_to_kilometers(self, value: float) -> float:
        """Convert distance from meters to kilometers."""
        return self.METERS_PER_METER * value * self.KILOMETERS_PER_METER

if __name__ == '__main__':
    converter = UnitConverter()
    
    # Sample values (hard-coded as per instructions, no interactive input)
    sample_meters = 100.5
    
    feet_result = converter.meters_to_feet(sample_meters)
    kilometers_result = converter.meters_to_kilometers(sample_meters)

    print(f"{sample_meters} meters is equal to {feet_result:.2f} feet.")
    print(f"{sample_meters} meters is equal to {kilometers_result:.6f} kilometers.")