import math

class VolumeConverter:
    """A highly reusable class to convert between various volume units."""
    
    # Constants (1 unit = X other unit)
    LITERS_PER_MILLILITER = 0.001      # liters per milliliter
    MILLILITERS_PER_LITER = 1000       # milliliters per liter
    
    CUBIC_METERS_PER_CU_INCH = (0.0254 ** 3) # cubic meters per cubic inch
    CU_INCHES_PER_CUBIC_METER = round(1 / (0.0254 ** 3), 6)

    def convert_liters_to_milliliters(self, liters: float) -> float:
        """Convert volume from liters to milliliters."""
        return liters * self.MILLILITERS_PER_LITER
    
    def convert_milliliters_to_liters(self, milliliters: float) -> float:
        """Convert volume from milliliters to liters."""
        return milliliters / self.MILLILITERS_PER_LITER

    def convert_cubic_inches_to_cubic_meters(self, cubic_inches: float) -> float:
        """Convert volume from cubic inches to cubic meters."""
        return cubic_inches * self.CUBIC_METERS_PER_CU_INCH
    
    def convert_cubic_meters_to_cubic_inches(self, cubic_meters: float) -> float:
        """Convert volume from cubic meters to cubic inches."""
        return cubic_meters / self.CU_INCHES_PER_CUBIC_METER

def main():
    # Create an instance of the converter class
    converter = VolumeConverter()

    # Sample values for testing - all hard-coded as per requirements
    sample_liters = 2.5
    sample_milliliters = 1000
    
    sample_cubic_inches = 1728  # exactly 1 cubic foot
    sample_cubic_meters = 1.0

    print("Volume Conversion Results:")
    
    # Test Liters to Milliliters conversion
    converted_ml = converter.convert_liters_to_milliliters(sample_liters)
    print(f"{sample_liters} liters is equal to {converted_ml} milliliters.")

    # Test Milliliters to Liters conversion (reverse check)
    back_converted_liters = converter.convert_milliliters_to_liters(sample_milliliters)
    assert abs(back_converted_liters - sample_liters) < 0.001, "Reverse conversion failed."

    # Test Cubic Meters to Cubic Inches conversion
    converted_cu_inches = converter.convert_cubic_meters_to_cubic_inches(sample_cubic_meters)
    
    # Test Cubic Inches to Cubic Meters conversion (reverse check with float precision allowed)
    back_converted_cubemeters = converter.convert_cubic_inches_to_cubic_meters(sample_cubic_inches)
    print(f"{sample_cu_inches} cubic inches is approximately {back_converted_cubemeters:.6f} cubic meters.")

if __name__ == '__main__':
    main()