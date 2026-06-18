class VolumeConverter:
    """A class to convert between volume units including liters/milliliters 
    and cubic meters/cubic inches."""
    
    def __init__(self):
        # Constants defining conversion factors relative to base unit (cubic meter)
        self.LITERS_PER_CUBIC_METER = 1000.0
        self.MILLILITERS_PER_LITER = 1000.0
        self.CUBIC_INCHES_PER_CUBIC_METRE = 6102374.40947

    def liters_to_milliliters(self, volume_liters: float) -> float:
        """Converts a given volume in liters to milliliters."""
        return volume_liters * self.MILLILITERS_PER_LITER

    def milliliters_to_liters(self, volume_milliliters: float) -> float:
        """Converts a given volume in milliliters to liters."""
        return volume_milliliters / self.MILLILITERS_PER_LITER

    def cubic_meters_to_cubic_inches(self, volume_cubic_meters: float) -> float:
        """Converts a given volume in cubic meters to cubic inches."""
        return volume_cubic_meters * self.CUBIC_INCHES_PER_CUBIC_METRE

    def cubic_inches_to_cubic_meters(self, volume_cubic_inches: float) -> float:
        """Converts a given volume in cubic inches to cubic meters."""
        return volume_cubic_inches / self.CUBIC_INCHES_PER_CUBIC_METRE

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = VolumeConverter()

    # Sample conversions between liters and milliliters
    liter_sample = 2.5
    ml_result = converter.liters_to_milliliters(liter_sample)
    
    print(f"Converting {liter_sample} Liters to Milliliters: {ml_result}")

    ml_back_sample = 1000.0
    l_result = converter.milliliters_to_liters(ml_back_sample)
    
    print(f"Converting {ml_back_sample} Milliliters to Liters: {l_result}")

    # Sample conversions between cubic meters and cubic inches
    
    m3_sample = 1.5
    ci_result = converter.cubic_meters_to_cubic_inches(m3_sample)
    
    print(f"Converting {m3_sample} Cubic Meters to Cubic Inches: {ci_result}")

    ci_back_sample = 2000000.0
    m3_result = converter.cubic_inches_to_cubic_meters(ci_back_sample)
    
    print(f"Converting {ci_back_sample} Cubic Inches to Cubic Meters: {m3_result}")