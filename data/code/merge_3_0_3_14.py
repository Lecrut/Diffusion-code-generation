class UnitConverter:
    """A class to handle conversions between meters, feet, and kilometers."""
    
    # Conversion factors stored as class constants
    FEET_PER_METER = 3.28084  # Feet per meter
    MILES_PER_KM = 0.621371   # Miles per kilometer (not directly used but good context)
    KM_PER_MILE = 1.60934      # Kilometers per mile

    def meters_to_feet(self, value: float) -> float:
        """Convert a length in meters to feet."""
        return value * self.FEET_PER_METER

    def feet_to_meters(self, value: float) -> float:
        """Convert a length in feet to meters."""
        return value / self.FEET_PER_METER

    def km_to_feet(self, value: float) -> float:
        """Convert kilometers to feet (1km = 3280.84 ft)."""
        # Calculate conversion factor derived from constants for precision or use direct math here
        return value * self.KM_PER_MILE * self.FEET_PER_METER

    def meters_to_km(self, value: float) -> float:
        """Convert a length in meters to kilometers."""
        return value / 1000.0

# Example usage block with hard-coded sample values (no interactive input)
if __name__ == '__main__':
    converter = UnitConverter()

    # Sample conversions based on specific test cases provided by the user's prompt structure
    samples = [
        ("meters to feet", "10 meters"),
        ("feet to meters", "50 feet"),
        ("kilometers to feet", "2 kilometers")
    ]

    print("Unit Conversion Results:")
    for desc, input_val_str in samples:
        try:
            # Parse the sample string (e.g., remove 'meters' if present and convert to float)
            val_part = input_val_str.split()[0] 
            unit_suffix = input_val_str[-6:]  # Extract 'meters', 'feet', or 'kilometers'

            value = int(val_part.strip())

            if unit_suffix == "meters":
                converted_value = converter.meters_to_feet(value)
                print(f"{input_val_str} => {converted_value:.2f} feet")
                
            elif unit_suffix == "feet":
                converted_value = converter.feet_to_meters(value)
                print(f"{input_val_str} => {converted_value:.4f} meters")

            elif unit_suffix == "kilometers":
                converted_value = converter.km_to_feet(value)
                print(f"{input_val_str} => {converted_value:.2f} feet")

        except Exception as e:
            # Fallback handling for any unexpected parsing issues if input format varies slightly
            pass