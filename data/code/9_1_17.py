class VolumeConverter:
    """
    A class to convert between volume units including liters, milliliters, 
    cubic meters, and cubic inches. It is designed to be object-oriented 
    and highly reusable by providing instance methods rather than static ones.
    
    Conversion factors used:
    - 1 liter = 1000 milliliters
    - 1 cubic meter = ~359.2704 cubic inches (exact factor derived from inch definition)
      Since 1 m = 39.3701 inches, then 1 m^3 = (39.3701)^3 in^3 ≈ 61023.744095 in^3
    
    Attributes: None

    Methods:
        - convert_liters_to_milliliters(liters): Returns liters * 1000
        - convert_milliliters_to_liters(milliliters): Returns milliliters / 1000
        - convert_cubic_meters_to_cubic_inches(cubic_meters): Converts using precise factor.
        - convert_cubic_inches_to_cubic_meters(inches): Inverse conversion.
    """

    # Constants for high precision conversions
    LITERS_TO_MILLILITERS_FACTOR = 1000.0
    
    # Conversion: 1 meter = 39.37007874 inches (international inch definition)
    METER_TO_INCHES_FACTOR = 39.37007874
    CUBIC_METERS_TO_CUBIC_INCHES_FACTOR = METER_TO_INCHES_FACTOR ** 3

    def convert_liters_to_milliliters(self, liters: float) -> float:
        """Converts a given volume in liters to milliliters."""
        return self._convert(liters, LITERS_TO_MILLILITERS_FACTOR)

    def convert_milliliters_to_liters(self, milliliters: float) -> float:
        """Converts a given volume in milliliters to liters."""
        # Using the inverse of the direct factor ensures precision consistency
        return self._convert(milliliters, 1.0 / LITERS_TO_MILLILITERS_FACTOR)

    def convert_cubic_meters_to_cubic_inches(self, cubic_meters: float) -> float:
        """Converts a given volume in cubic meters to cubic inches."""
        return self._convert(cubic_meters, CUBIC_METERS_TO_CUBIC_INCHES_FACTOR)

    def convert_cubic_inches_to_cubic_meters(self, cubic_inches: float) -> float:
        """Converts a given volume in cubic inches to cubic meters."""
        # Using the inverse of the direct factor ensures precision consistency
        return self._convert(cubic_inches, 1.0 / CUBIC_METERS_TO_CUBIC_INCHES_FACTOR)

    def _convert(self, value: float, factor: float) -> float:
        """Internal helper method to perform multiplication conversion."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        return round(float(value * factor), 6)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    
    converter = VolumeConverter()

    print("--- Liters to Milliliters ---")
    liters_val = 2.5
    ml_result = converter.convert_liters_to_milliliters(liters_val)
    print(f"{liters_val} liters is {ml_result} milliliters.")

    print("\n--- Milliliters to Liters ---")
    ml_input = 3750
    l_result = converter.convert_milliliters_to_liters(ml_input)
    print(f"{ml_input} milliliters is {l_result} liters.")

    print("\n--- Cubic Meters to Cubic Inches ---")
    m3_val = 1.2
    in3_result = converter.convert_cubic_meters_to_cubic_inches(m3_val)
    print(f"{m3_val} cubic meters is approximately {in3_result:.4f} cubic inches.")

    print("\n--- Cubic Inches to Cubic Meters ---")
    in3_input = 100.5
    m3_result = converter.convert_cubic_inches_to_cubic_meters(in3_input)
    print(f"{in3_input} cubic inches is approximately {m3_result:.6f} cubic meters.")

    # Round-trip verification example (approximate due to floating point precision limits in different unit systems, 
    # though the conversion factors are exact based on definitions)
    original_m3 = 0.5
    converted_in3 = converter.convert_cubic_meters_to_cubic_inches(original_m3)
    back_to_m3 = converter.convert_cubic_inches_to_cubic_meters(converted_in3)
    
    print(f"\n--- Verification: {original_m3} m³ -> in³ -> m³ ---")
    print(f"Original (m³): {original_m3}")
    print(f"After conversion back to m³: {back_to_m3:.6f}")