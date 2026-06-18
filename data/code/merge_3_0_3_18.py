class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""
    
    # Conversion factors stored as class constants (relative to meters)
    METERS_PER_FOOT = 0.3048
    KILOMETERS_PER_METER = 1e-3
    
    def convert_meters_to_feet(self, value: float) -> float:
        """Convert distance in meters to feet."""
        return self.METERS_PER_FOOT * value

    def convert_meters_to_kilometers(self, value: float) -> float:
        """Convert distance in meters to kilometers."""
        return self.KILOMETERS_PER_METER * value

if __name__ == '__main__':
    converter = UnitConverter()
    
    # Sample values - no interactive input
    sample_meters_1 = 50.234       # A short distance in meters
    sample_feet = 200              # An approximate length in feet (approx 60m)
    sample_km = 0.75               # A medium run distance
    
    print("UnitConverter - Conversion Results")
    
    # Convert the first meter value to other units
    converted_ft_1 = converter.convert_meters_to_feet(sample_meters_1)
    converted_km_1 = converter.convert_meters_to_kilometers(sample_meters_1)
    print(f"{sample_meters_1:.4f} meters is equivalent to:")
    print(f"  {converted_ft_1:.2f} feet")
    print(f"  {converted_km_1:.6f} kilometers\n")

    # Demonstrate conversion from the other units back (using constants)
    print("--- Reverse Conversions using Constants ---")
    
    ft_to_m = sample_feet / converter.METERS_PER_FOOT
    km_to_m = sample_km / converter.KILOMETERS_PER_METER
    
    print(f"{sample_feet} feet is equivalent to {ft_to_m:.2f} meters.")
    print(f"{sample_km} kilometers is equivalent to {km_to_m * 1000:.4f} meters (or approx {converter.METERS_PER_FOOT * km_to_m / converter.KILOMETERS_PER_METER**(-3)} feet).")