class UnitConverter:
    # Conversion factors to meters (1 unit = factor * meter)
    METERS_PER_METER = 1.0
    METERS_PER_FOOT = 0.3048
    METERS_PER_KILOMETER = 1000.0
    
    def convert_to_meters(self, value: float, from_unit: str) -> float:
        """Convert a given length to meters based on the source unit."""
        if from_unit == 'm':
            return value * self.METERS_PER_METER
        elif from_unit == 'ft':
            return value * self.METERS_PER_FOOT
        elif from_unit == 'km':
            return value * self.METERS_PER_KILOMETER
        else:
            raise ValueError(f"Unsupported unit for conversion: {from_unit}")

    def convert_to_feet(self, meters_value: float) -> float:
        """Convert a length in meters to feet."""
        return meters_value / self.METERS_PER_FOOT

    def convert_to_kilometers(self, meters_value: float) -> float:
        """Convert a length in meters to kilometers."""
        return meters_value / self.METERS_PER_KILOMETER

if __name__ == '__main__':
    # Hard-coded sample values for testing
    converter = UnitConverter()

    # Sample conversions from different units to meters
    result_m_from_ft = converter.convert_to_meters(10, 'ft')  # Expected: ~3.048
    print(f"10 feet in meters: {result_m_from_ft}")

    result_km_in_km = converter.convert_to_kilometers(result_m_from_ft)  # Convert back to km
    print(f"{result_m_from_ft} meters in kilometers: {result_km_in_km:.6f}")