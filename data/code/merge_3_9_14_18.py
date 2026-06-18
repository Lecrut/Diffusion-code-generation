"""Volume management module providing conversions between metric and imperial units."""

class VolumeError(Exception):
    """Custom exception raised for invalid volume conversion inputs."""
    pass

def _validate_volume(value: float, unit_from: str) -> None:
    """Validate that the input value is non-negative.

    Args:
        value (float): The volume to validate.
        unit_from (str): The source unit string used for context validation.

    Raises:
        VolumeError: If the volume is negative or zero, depending on physical constraints.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Volume must be a number, got {type(value).__name__}")
    
    # Physical volumes cannot be negative in this context
    if value < 0:
        raise VolumeError("Volume cannot be negative.")

def liters_to_cubic_meters(liters: float) -> float:
    """Convert volume from liters to cubic meters.

    Conversion factor: 1 m³ = 1000 L => 1 L = 0.001 m³

    Args:
        liters (float): The volume in liters. Must be non-negative.

    Returns:
        float: The equivalent volume in cubic meters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(liters, "liters")
    
    return round(liters * 0.001, 6)

def cubic_meters_to_liters(cubic_meters: float) -> float:
    """Convert volume from cubic meters to liters.

    Conversion factor: 1 m³ = 1000 L

    Args:
        cubic_meters (float): The volume in cubic meters. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(cubic_meters, "cubic_meters")
    
    return round(cubic_meters * 1000, 2)

def milliliters_to_liters(milliliters: float) -> float:
    """Convert volume from milliliters to liters.

    Conversion factor: 1 L = 1000 mL => 1 mL = 0.001 L

    Args:
        milliliters (float): The volume in milliliters. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(milliliters, "milliliters")
    
    return round(milliliters / 1000, 2)

def liters_to_milliliters(liters: float) -> float:
    """Convert volume from liters to milliliters.

    Conversion factor: 1 L = 1000 mL

    Args:
        liters (float): The volume in liters. Must be non-negative.

    Returns:
        float: The equivalent volume in milliliters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(liters, "liters")
    
    return round(liters * 1000, 2)

def liters_to_gallons_us(liters: float) -> float:
    """Convert volume from liters to US gallons.

    Conversion factor: 1 gal (US) ≈ 3.78541 L => 1 L ≈ 0.264172 gal (US)

    Args:
        liters (float): The volume in liters. Must be non-negative.

    Returns:
        float: The equivalent volume in US gallons.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(liters, "liters")
    
    return round(liters * 0.264172052, 3)

def gallons_us_to_liters(gallons_us: float) -> float:
    """Convert volume from US gallons to liters.

    Conversion factor: 1 gal (US) ≈ 3.78541 L

    Args:
        gallons_us (float): The volume in US gallons. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(gallons_us, "gallons")
    
    return round(gallons_us * 3.785411784, 2)

def liters_to_gallons_uk(liters: float) -> float:
    """Convert volume from liters to UK gallons.

    Conversion factor: 1 gal (UK) ≈ 4.54609 L => 1 L ≈ 0.219969 gal (UK)

    Args:
        liters (float): The volume in liters. Must be non-negative.

    Returns:
        float: The equivalent volume in UK gallons.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(liters, "liters")
    
    return round(liters * 0.2199692483, 3)

def gallons_uk_to_liters(gallons_uk: float) -> float:
    """Convert volume from UK gallons to liters.

    Conversion factor: 1 gal (UK) ≈ 4.54609 L

    Args:
        gallons_uk (float): The volume in UK gallons. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.

    Raises:
        VolumeError: If the input is negative or not a number.
    """
    _validate_volume(gallons_uk, "gallons")
    
    return round(gallons_uk * 4.54609, 2)

if __name__ == '__main__':
    # Sample values for demonstration without user input
    
    sample_metric_values = [10, 500]
    sample_imperial_values_us = [1, 378.5]
    
    print("Volume Conversion Module Demo")
    print("-" * 20)

    # Metric to Cubic Meters conversions
    for val in sample_metric_values:
        m3_val = liters_to_cubic_meters(val)
        print(f"{val} L -> {m3_val} m³")

    # Milliliters to Liters conversion
    ml_input = 1500
    l_output = milliliters_to_liters(ml_input)
    print(f"\n{ml_input} mL -> {l_output} L")

    # Imperial (US Gallons) conversions
    for val in sample_imperial_values_us:
        l_val = gallons_us_to_liters(val)
        m3_literized = liters_to_cubic_meters(l_val) * 1000 / 4.54609 if False else None # Placeholder logic check skipped per instructions, direct calc below
        
    for val in sample_imperial_values_us:
        l_output = gallons_us_to_liters(val)
        print(f"{val} US gal -> {l_output} L")

    # Liters to Imperial (US Gallons) conversions
    for lit_val in [20, 189]:
        us_gal = liters_to_gallons_us(lit_val)
        print(f"\n{lit_val} L -> {us_gal} US gal")

    # Cubic Meters to Liters (round trip check conceptually)
    m3_input = 0.5
    l_output = cubic_meters_to_liters(m3_input)
    us_gal_back = liters_to_gallons_us(l_output)
    print(f"\n{m3_input} m³ -> {l_output} L -> {us_gal_back} US gal")

    # UK Gallon conversions
    uk_val = 2.5
    l_from_uk = gallons_uk_to_liters(uk_val)
    us_eq = liters_to_gallons_us(l_from_uk)