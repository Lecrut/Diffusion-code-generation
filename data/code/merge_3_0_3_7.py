class UnitConverter:
    # Conversion factors to meters (1 unit = X meters)
    METERS_PER_METER = 1.0
    METERS_PER_FEET = 0.3048
    METERS_PER_KILOMETER = 1000.0
    
    def convert_to_meters(self, value: float, from_unit: str) -> float:
        """Convert a given length to meters based on the source unit."""
        if from_unit == 'm':
            return value * self.METERS_PER_METER
        elif from_unit == 'ft':
            return value * self.METERS_PER_FEET
        elif from_unit == 'km':
            return value * self.METERS_PER_KILOMETER
        else:
            raise ValueError(f"Unsupported unit for conversion: {from_unit}")

    def convert_to_feet(self, meters_value: float) -> float:
        """Convert a length in meters to feet."""
        return meters_value / self.METERS_PER_FEET

    def convert_to_kilometers(self, meters_value: float) -> float:
        """Convert a length in meters to kilometers."""
        return meters_value / self.METERS_PER_KILOMETER

if __name__ == '__main__':
    converter = UnitConverter()
    
    # Sample conversions using hard-coded values
    sample_meters = 10.5
    
    print(f"Original value: {sample_meters} m")
    print(f"In feet: {converter.convert_to_feet(sample_meters):.4f}")
    print(f"In kilometers: {converter.convert_to_kilometers(sample_meters):.6f}")
    
    # Convert from other units to meters as a demonstration
    sample_feet = 30.0
    converted_from_ft = converter.convert_to_meters(sample_feet, 'ft')
    print(f"\nConverted {sample_feet} ft to meters: {converted_from_ft:.4f}")