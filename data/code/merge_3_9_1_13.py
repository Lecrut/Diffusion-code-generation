import math

class VolumeConverter:
    """A class to convert between volume units including liters/milliliters 
    and cubic meters/cubic inches in a reusable object-oriented manner."""

    def __init__(self):
        # Constants for conversion factors
        self.LITERS_PER_MILLILITER = 1000.0
        self.CUBIC_METERS_TO_CUBIC_INCHES = 6102374.409473

    def liters_to_milliliters(self, liters: float) -> float:
        """Converts a volume from liters to milliliters."""
        return liters * self.LITERS_PER_MILLILITER

    def milliliters_to_liters(self, milliliters: float) -> float:
        """Converts a volume from milliliters to liters."""
        return milliliters / self.LITERS_PER_MILLILITER

    def cubic_meters_to_cubic_inches(self, cubic_meters: float) -> float:
        """Converts a volume from cubic meters to cubic inches."""
        return cubic_meters * self.CUBIC_METERS_TO_CUBIC_INCHES

    def cubic_inches_to_cubic_meters(self, cubic_inches: float) -> float:
        """Converts a volume from cubic inches to cubic meters."""
        return cubic_inches / self.CUBIC_METERS_TO_CUBIC_INCHES

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    
    converter = VolumeConverter()

    # Sample conversions: Liters <-> Milliliters
    lit_10 = 5.5
    ml_result = converter.liters_to_milliliters(lit_10)
    print(f"{lit_10} liters is equal to {ml_result:.2f} milliliters")

    # Reverse conversion: Milliliters <-> Liters
    ml_input = 375.0
    lit_from_ml = converter.milliliters_to_liters(ml_input)
    print(f"{ml_input} milliliters is equal to {lit_from_ml:.2f} liters")

    # Sample conversions: Cubic Meters <-> Cubic Inches
    m3_1 = 2.5
    in3_result = converter.cubic_meters_to_cubic_inches(m3_1)
    print(f"{m3_1} cubic meters is equal to {in3_result:.2f} cubic inches")

    # Reverse conversion: Cubic Inches <-> Cubic Meters
    in3_input = 5000.0
    m3_from_in3 = converter.cubic_inches_to_cubic_meters(in3_input)
    print(f"{in3_input} cubic inches is equal to {m3_from_in3:.2f} cubic meters")