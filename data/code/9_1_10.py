import math

class VolumeConverter:
    """A class to convert between volume units including liters, milliliters, cubic meters, and cubic inches."""
    
    # Conversion constants (1 unit = equivalent value in target base)
    _LITERS_TO_MILLILITERS_RATIO = 1000.0
    _CUBIC_METERS_TO_CUBIC_INCHES_RATIO = math.pow(35.2778, 3)

    def liters_to_milliliters(self, value: float) -> float:
        """Convert a volume from liters to milliliters."""
        return round(value * self._LITERS_TO_MILLILITERS_RATIO, decimals=6)

    def milliliters_to_liters(self, value: float) -> float:
        """Convert a volume from milliliters to liters."""
        return round(value / self._LITERS_TO_MILLILITERS_RATIO, decimals=6)

    def cubic_meters_to_cubic_inches(self, value: float) -> float:
        """Convert a volume from cubic meters to cubic inches."""
        return round(value * self._CUBIC_METERS_TO_CUBIC_INCHES_RATIO, decimals=6)

    def cubic_inches_to_cubic_meters(self, value: float) -> float:
        """Convert a volume from cubic inches to cubic meters."""
        return round(value / self._CUBIC_METERS_TO_CUBIC_INCHES_RATIO, decimals=10)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    
    converter = VolumeConverter()

    print("Volume Conversion Examples")
    print("-" * 30)

    # Liters to Milliliters examples
    l_to_ml_1 = converter.liters_to_milliliters(2.5)
    l_to_ml_2 = converter.liters_to_milliliters(100)
    
    print(f"Liters -> Milliliters:")
    print(f"  {l_to_ml_1:.6f} liters is equivalent to {l_to_ml_1} milliliters")
    print(f"  {l_to_ml_2:.6f} liters is equivalent to {l_to_ml_2} milliliters")

    # Milliliters back to Liters examples (reversibility check)
    ml_back_l = converter.milliliters_to_liters(l_to_ml_1)
    
    print(f"\nMilliliters -> Liters:")
    print(f"  {l_to_ml_1} milliliters is equivalent to {ml_back_l:.6f} liters")

    # Cubic Meters to Cubic Inches examples
    cm3_to_ci = converter.cubic_meters_to_cubic_inches(0.5)
    
    print("\nCubic Meters -> Cubic Inches:")
    print(f"  {cm3_to_ci:.2e} cubic meters is equivalent to {int(cm3_to_ci)} cubic inches")

    # Cubic Inches back to Cubic Meters examples (reversibility check)
    ci_back_cm3 = converter.cubic_inches_to_cubic_meters(int(cm3_to_ci))
    
    print("\nCubic Inches -> Cubic Meters:")
    print(f"  {int(cm3_to_ci)} cubic inches is equivalent to {ci_back_cm3:.2e} cubic meters")

    # Demonstrate method reuse with different values
    sample_volumes = [1, 50, 75.5]
    
    print("\nBatch Conversion (Liters -> Milliliters):")
    for vol in sample_volumes:
        result = converter.liters_to_milliliters(vol)
        print(f"  {vol} L => {result:.6f} mL")