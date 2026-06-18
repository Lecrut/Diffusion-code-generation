class VolumeConverter:
    """A class to convert between volume units including liters/milliliters 
    and cubic meters/cubic inches."""
    
    # Conversion constants
    MILLILITERS_PER_LITER = 1000
    CUBIC_INCHES_PER_CUBIC_METER = (35.489672)

    def __init__(self):
        """Initialize the VolumeConverter instance with default conversion factors."""
        pass

    def liters_to_milliliters(self, liters: float) -> float:
        """Convert a volume from liters to milliliters.

        Args:
            liters (float): The volume in liters.

        Returns:
            float: The equivalent volume in milliliters.
        """
        return liters * self.MILLILITERS_PER_LITER

    def milliliters_to_liters(self, milliliters: float) -> float:
        """Convert a volume from milliliters to liters.

        Args:
            milliliters (float): The volume in milliliters.

        Returns:
            float: The equivalent volume in liters.
        """
        return milliliters / self.MILLILITERS_PER_LITER

    def cubic_meters_to_cubic_inches(self, cubic_meters: float) -> float:
        """Convert a volume from cubic meters to cubic inches.

        Args:
            cubic_meters (float): The volume in cubic meters.

        Returns:
            float: The equivalent volume in cubic inches.
        """
        return cubic_meters * self.CUBIC_INCHES_PER_CUBIC_METER

    def cubic_inches_to_cubic_meters(self, cubic_inches: float) -> float:
        """Convert a volume from cubic inches to cubic meters.

        Args:
            cubic_inches (float): The volume in cubic inches.

        Returns:
            float: The equivalent volume in cubic meters.
        """
        return cubic_inches / self.CUBIC_INCHES_PER_CUBIC_METER

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    converter = VolumeConverter()

    # Sample conversions between liters and milliliters
    liter_value = 2.5
    ml_result = converter.liters_to_milliliters(liter_value)
    
    print(f"Converting {liter_value} liters to milliliters: {ml_result}")

    ml_input = 7500
    l_result = converter.milliliters_to_liters(ml_input)
    
    print(f"Converting {ml_input} milliliters to liters: {l_result}")

    # Sample conversions between cubic meters and cubic inches
    m3_value = 1.2
    in3_result = converter.cubic_meters_to_cubic_inches(m3_value)
    
    print(f"Converting {m3_value} cubic meters to cubic inches: {in3_result}")

    in3_input = 50000
    m3_result = converter.cubic_inches_to_cubic_meters(in3_input)
    
    print(f"Converting {in3_input} cubic inches to cubic meters: {m3_result}")