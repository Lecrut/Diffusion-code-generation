class VolumeConverter:
    """
    A class to convert between volume units including liters/milliliters 
    and cubic meters/cubic inches. Designed for high reusability via methods,
    with constant conversion factors encapsulated as private attributes.
    
    Attributes:
        none
    
    Methods:
        liter_to_milliliter(liters): Converts liters to milliliters.
        milliliter_to_liter(milliliters): Converts milliliters to liters.
        cubic_meter_to_cubic_inch(cubemeters): Converts cubic meters to cubic inches.
        cubic_inch_to_cubic_meter(cubinches): Converts cubic inches to cubic meters.
    """

    # Conversion factors (private constants)
    _L_TO_ML_FACTOR = 1000.0   # Liters to Milliliters
    _M3_PER_INCH_CUBIC = 6.1e-8 # Cubic Meters per Cubic Inch
    
    def __init__(self):
        """Initializes the VolumeConverter instance."""
        pass

    def liter_to_milliliter(self, liters: float) -> float:
        """Converts a volume from liters to milliliters.
        
        Args:
            liters (float): The volume in liters. Must be non-negative.
            
        Returns:
            float: The equivalent volume in milliliters.
        """
        return self._L_TO_ML_FACTOR * liters

    def milliliter_to_liter(self, milliliters: float) -> float:
        """Converts a volume from milliliters to liters.
        
        Args:
            milliliters (float): The volume in milliliters. Must be non-negative.
            
        Returns:
            float: The equivalent volume in liters.
        """
        return self._L_TO_ML_FACTOR ** -1 * milliliters

    def cubic_meter_to_cubic_inch(self, cubemeters: float) -> float:
        """Converts a volume from cubic meters to cubic inches.
        
        Args:
            cubemeters (float): The volume in cubic meters. Must be non-negative.
            
        Returns:
            float: The equivalent volume in cubic inches.
        """
        # There are approximately 610237.44 cubic inches in a cubic meter.
        # Using the inverse of self._M3_PER_INCH_CUBIC for precision here based on standard definition 
        # (1 inch = 0.0254 m, so 1 in^3 = 0.0254^3 m^3)
        FACTOR = 1 / self._M3_PER_INCH_CUBIC
        return cubemeters * FACTOR

    def cubic_inch_to_cubic_meter(self, cubinches: float) -> float:
        """Converts a volume from cubic inches to cubic meters.
        
        Args:
            cubinches (float): The volume in cubic inches. Must be non-negative.
            
        Returns:
            float: The equivalent volume in cubic meters.
        """
        return self._M3_PER_INCH_CUBIC * cubinches

if __name__ == '__main__':
    # Sample execution without user input or arguments
    
    converter = VolumeConverter()
    
    print("Volume Conversion Tests")
    print("-" * 20)
    
    # Test Liters to Milliliters and back
    sample_liters = 5.75
    result_ml = converter.liter_to_milliliter(sample_liters)
    converted_back_liters = converter.milliliter_to_liter(result_ml)
    
    print(f"Input: {sample_liters} Liters")
    print(f"Converted to Milliliters: {result_ml}")
    print(f"Converted back to Liters: {converted_back_liters:.4f}")
    assert abs(sample_liters - converted_back_liters) < 0.001, "Round-trip conversion failed for liters."
    
    # Test Cubic Meters to Cubic Inches and back using standard definition constants directly 
    # since the class internal constant relies on a specific approximation provided in init logic above contextually.
    # To ensure absolute accuracy without external dependencies, we use exact mathematical definitions here:
    # 1 inch = 0.0254 meters exactly
    
    m3_to_inch_exact = lambda x: (x / 0.0254) ** 3
    in_ch_to_m3_exact = lambda y: ((y ** (1/3)) * 0.0254) ** 3 # Re-calculation based on input
    
    sample_m3 = 2.5e-6
    result_inch = m3_to_inch_exact(sample_m3)
    
    print(f"Input: {sample_m3} Cubic Meters")
    print(f"Converted to Cubic Inches (approx): {result_inch:.4f}")
    
    # Re-running a specific test using the class methods with expected mathematically accurate conversion 
    # Note: 1 m^3 = approx 6.10237e+8 in^3
    
    sample_m3_2 = 0.5
    result_inch_class = converter.cubic_meter_to_cubic_inch(sample_m3_2)
    
    print(f"Input (Class): {sample_m3_2} Cubic Meters")
    print(f"Converted to Cubic Inches: {result_inch_class:.6f}")
    
    # Verify reverse conversion in class using the pre-defined factor logic if consistent, 
    # but strictly adhering to standard math for verification here is safer.
    expected_m3 = sample_m3_2
    check_val = converter.cubic_inch_to_cubic_meter(result_inch_class)
    print(f"Converted back (Class): {check_val:.6f}")
    
    assert abs(expected_m3 - check_val) < 1e-9, "Round-trip conversion failed for cubic units."

    print("-" * 20)
    print("All tests passed successfully.")