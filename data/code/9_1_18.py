class VolumeConverter:
    """
    A class to convert between different volume units using standard conversion factors.
    
    Methods support conversions between liters (L) and milliliters (mL), 
    as well as cubic meters (m³) and cubic inches (in³).
    The implementation uses object-oriented principles for reusability.
    """

    # Conversion constants defined once to ensure precision and reuse
    LITERS_TO_MILLILITERS = 1000.0
    
    MILLILITERS_TO_LITERS = 0.001

    CUBIC_METERS_TO_CUBIC_INCHES = 610237.440947
    CUBIC_INCHES_TO_CUBIC_METERS = 1 / (CUBIC_METERS_TO_CUBIC_INCHES)

def convert_liters_to_milliliters(liters: float) -> float:
    """Convert a volume from liters to milliliters."""
    return liters * VolumeConverter.LITERS_TO_MILLILITERS

def convert_milliliters_to_liters(milliliters: float) -> float:
    """Convert a volume from milliliters to liters."""
    return milliliters * VolumeConverter.MILLILITERS_TO_LITERS

def convert_cubic_metres_to_cubic_inches(cubic_metres: float) -> float:
    """Convert a volume from cubic meters to cubic inches."""
    return cubic_metres * VolumeConverter.CUBIC_METERS_TO_CUBIC_INCHES

def convert_cubic_inches_to_cubic_metres(cubic_inches: float) -> float:
    """Convert a volume from cubic inches to cubic meters."""
    return cubic_inches * VolumeConverter.CUBIC_INCHES_TO_CUBIC_METRES

if __name__ == '__main__':
    pass
