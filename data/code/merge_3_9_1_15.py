class VolumeConverter:
    """A class to convert between different volume units."""
    
    # Conversion constants (1 unit = target_units)
    LITERS_TO_MILLILITERS = 1000
    MILLILITERS_TO_LITERS = 1 / 1000
    
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.7440947318 # Approximate: (1 m)^3 * (39.37 in/m)^3
    CUBIC_INCHES_TO_CUBIC_METERS = 1 / 61023.7440947318

    def liters_to_milliliters(self, value_liters: float) -> float:
        """Convert volume from liters to milliliters."""
        return self.LITERS_TO_MILLILITERS * value_liters

    def milliliters_to_liters(self, value_ml: float) -> float:
        """Convert volume from milliliters to liters."""
        return self.MILLILITERS_TO_LITERS * value_ml

    def cubic_meters_to_cubic_inches(self, value_m3: float) -> float:
        """Convert volume from cubic meters to cubic inches."""
        return self.CUBIC_METERS_TO_CUBIC_INCHES * value_m3

    def cubic_inches_to_cubic_meters(self, value_in3: float) -> float:
        """Convert volume from cubic inches to cubic meters."""
        return self.CUBIC_INCHES_TO_CUBIC_METERS * value_in3

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    converter = VolumeConverter()

    print("=== Liters and Milliliters Conversion ===")
    
    # Sample: Convert 5 liters to milliliters
    val_liters = 5.0
    result_ml = converter.liters_to_milliliters(val_liters)
    print(f"{val_liters} liters is equal to {result_ml:.2f} milliliters")

    # Sample: Convert 1000 milliliters back to liters (should be ~5.0)
    val_ml = 1000.0
    result_back_liters = converter.milliliters_to_liters(val_ml)
    print(f"{val_ml} milliliters is equal to {result_back_liters:.2f} liters")

    print("\n=== Cubic Meters and Cubic Inches Conversion ===")
    
    # Sample: Convert 1 cubic meter to cubic inches
    val_m3 = 1.0
    result_in3 = converter.cubic_meters_to_cubic_inches(val_m3)
    print(f"{val_m3} cubic meters is equal to {result_in3:.2f} cubic inches")

    # Sample: Convert a large number of cubic inches back to cubic meters
    val_in3 = 10000.0
    result_back_m3 = converter.cubic_inches_to_cubic_meters(val_in3)
    print(f"{val_in3:.2f} cubic inches is equal to {result_back_m3:.6e} cubic meters")

    # Demonstrate reusability by converting a chain of units (Liters -> mL -> back to Liters via math check implicitly handled in separate calls if needed, 
    # but here we just show independent conversions)
    
    print("\n=== Reusability Check ===")
    original_volume = 2.5
    
    # Convert liters to milliliters using the same object instance multiple times without side effects
    ml_result_1 = converter.liters_to_milliliters(original_volume)
    ml_result_2 = converter.milliliters_to_liters(ml_result_1) 
    
    print(f"Original: {original_volume} L")
    print(f"After conversion chain (L -> mL -> L): {ml_result_2:.4f} L")
    
    # Verify precision within floating point limits
    if abs(original_volume - ml_result_2) < 0.001:
        print("Conversion accuracy verified.")