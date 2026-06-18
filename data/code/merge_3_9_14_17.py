"""Volume management module with unit conversion capabilities."""

class VolumeError(Exception):
    """Custom exception raised for invalid volume conversions."""
    pass

def _validate_volume(value: float, min_val: float = 0) -> None:
    """Validate that the input value is a non-negative number.

    Args:
        value (float): The volume to validate.
        min_val (float): Minimum acceptable value (default is 0).

    Raises:
        VolumeError: If the value is less than min_val or not numeric.
    """
    if isinstance(value, float) and value < min_val:
        raise VolumeError(f"Volume cannot be less than {min_val}.")

def liters_to_cubic_meters(liters: float) -> float:
    """Convert volume from liters to cubic meters.

    Conversion factor: 1 L = 0.001 m³

    Args:
        liters (float): Volume in liters. Must be >= 0.

    Returns:
        float: Equivalent volume in cubic meters.

    Raises:
        VolumeError: If the input is invalid or negative.
    """
    _validate_volume(liters)
    return liters * 0.001

def cubic_meters_to_liters(cubic_meters: float) -> float:
    """Convert volume from cubic meters to liters.

    Conversion factor: 1 m³ = 1000 L

    Args:
        cubic_meters (float): Volume in cubic meters. Must be >= 0.

    Returns:
        float: Equivalent volume in liters.

    Raises:
        VolumeError: If the input is invalid or negative.
    """
    _validate_volume(cubic_meters)
    return cubic_meters * 1000

def milliliters_to_liters(milliliters: float) -> float:
    """Convert volume from milliliters to liters.

    Conversion factor: 1 mL = 0.001 L

    Args:
        milliliters (float): Volume in milliliters. Must be >= 0.

    Returns:
        float: Equivalent volume in liters.

    Raises:
        VolumeError: If the input is invalid or negative.
    """
    _validate_volume(milliliters)
    return milliliters / 1000

def liters_to_milliliters(liters: float) -> float:
    """Convert volume from liters to milliliters.

    Conversion factor: 1 L = 1000 mL

    Args:
        liters (float): Volume in liters. Must be >= 0.

    Returns:
        float: Equivalent volume in milliliters.

    Raises:
        VolumeError: If the input is invalid or negative.
    """
    _validate_volume(liters)
    return liters * 1000

def cubic_meters_to_gallons(cubic_meters: float, us_fluid=True) -> float:
    """Convert volume from cubic meters to US gallons (default).

    Conversion factor: 1 m³ ≈ 264.172052 US gal
                            or 1 m³ ≈ 283.97479 UK gal if us_fluid=False

    Args:
        cubic_meters (float): Volume in cubic meters. Must be >= 0.
        us_fluid (bool): If True, convert to US gallons; otherwise UK gallons. Default is True.

    Returns:
        float: Equivalent volume in gallons.

    Raises:
        VolumeError: If the input is invalid or negative.
    """
    _validate_volume(cubic_meters)
    if us_fluid:
        return cubic_meters * 264.1720523589
    else:
        return cubic_meters * 283.97479

if __name__ == '__main__':
    pass
