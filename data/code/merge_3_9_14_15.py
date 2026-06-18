"""
Volume Management Module

This module provides functionality to convert volume measurements between metric 
(Liters, milliliters, cubic meters) and imperial (Liters, gallons) units.
All constants are derived from standard conversion factors defined by the US National Institute of Standards and Technology.
"""

# Define precise conversion factors based on NIST standards
METRIC_TO_IMPERIAL_GALLONS = 0.264172052358148 # 1 m³ ≈ 264.17 gallons, but using direct L to gal for simplicity in logic below
IMPERIAL_METRIC_LITERS_PER_GALON = 3.785411784       # 1 gallon (US) is exactly this many liters

# Constants for volume calculations based on definitions:
# - 1 cubic meter (m³) = 1000 Liters (L)
# - 1 Liter (L) = 1000 milliliters (mL)
# - 1 gallon (US, liquid) ≈ 3.785411784 Liters

METER_TO_LITERS_FACTOR = 1000        # m³ to L conversion factor
LITER_TO_MILLILITER_FACTOR = 1000    # L to mL conversion factor

def cubic_meters_to_liters(volume_cubic_meters: float) -> float:
    """Convert volume from cubic meters (m³) to liters (L).

    Args:
        volume_cubic_meters (float): The volume in cubic meters. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.
    
    Raises:
        ValueError: If the input is negative.
    
    Examples:
        >>> convert_volume(1)
        1000.0
        >>> convert_volume(-5)
        Traceback (most recent call last): ...
        ValueError: Volume cannot be negative.
    """
    if volume_cubic_meters < 0:
        raise ValueError("Volume cannot be negative.")
    
    return volume_cubic_meters * METER_TO_LITERS_FACTOR

def liters_to_gallons(volume_liters: float) -> float:
    """Convert volume from liters (L) to US gallons.

    Args:
        volume_liters (float): The volume in liters. Must be non-negative.

    Returns:
        float: The equivalent volume in US gallons.
    
    Raises:
        ValueError: If the input is negative.
    """
    if volume_liters < 0:
        raise ValueError("Volume cannot be negative.")
    
    return volume_liters / IMPERIAL_METRIC_LITERS_PER_GALON

def milliliters_to_gallons(volume_milliliters: float) -> float:
    """Convert volume from milliliters (mL) to US gallons.

    Args:
        volume_milliliters (float): The volume in milliliters. Must be non-negative.

    Returns:
        float: The equivalent volume in US gallons.
    
    Raises:
        ValueError: If the input is negative.
    """
    if volume_milliliters < 0:
        raise ValueError("Volume cannot be negative.")
    
    # Convert mL to L first, then to gallons
    liters = volume_milliliters / LITER_TO_MILLILITER_FACTOR
    return liters / IMPERIAL_METRIC_LITERS_PER_GALON

def cubic_meters_to_gallons(volume_cubic_meters: float) -> float:
    """Convert volume from cubic meters (m³) to US gallons.

    This is a convenience function that chains the conversion through liters.

    Args:
        volume_cubic_meters (float): The volume in cubic meters. Must be non-negative.

    Returns:
        float: The equivalent volume in US gallons.
    
    Raises:
        ValueError: If the input is negative.
    """
    if volume_cubic_meters < 0:
        raise ValueError("Volume cannot be negative.")
    
    return cubic_meters_to_liters(volume_cubic_meters) / IMPERIAL_METRIC_LITERS_PER_GALON

def gallons_to_liters(gallons_volume: float) -> float:
    """Convert volume from US gallons to liters (L).

    Args:
        gallons_volume (float): The volume in US gallons. Must be non-negative.

    Returns:
        float: The equivalent volume in liters.
    
    Raises:
        ValueError: If the input is negative.
    """
    if gallons_volume < 0:
        raise ValueError("Volume cannot be negative.")
    
    return gallons_volume * IMPERIAL_METRIC_LITERS_PER_GALON

def main():
    """Run sample conversions to demonstrate functionality."""
    # Metric inputs for demonstration
    metric_cubic_meters = 2.5
    
    print(f"Input: {metric_cubic_meters} m³")
    
    liters_value = cubic_meters_to_liters(metric_cubic_meters)
    gallons_value = cubic_meters_to_gallons(metric_cubic_meters)
    
    print(f"{liters_value:.2f} Liters (L)")
    print(f"{gallons_value:.4f} US Gallons")
    
    # Additional sample conversions from different units
    
    metric_liters_input = 50.789136
    metric_milliliters_input = 125.0 
    
    print("\nInput: {:.6f} L".format(metric_liters_input))
    gal_from_l = liters_to_gallons(metric_liters_input)
    
    print(f"{gal_from_l:.4f} US Gallons")

    print("\nInput: {} mL".format(metric_milliliters_input))
    gal_from_ml = milliliters_to_gallons(metric_milliliters_input)
    
    print(f"{gal_from_ml:.6f} US Gallons")
    
    # Reverse conversions from gallons
    
    gallon_sample = 10.5 
    
    print("\nInput: {} US Gallons".format(gallon_sample))
    l_from_gal = gallons_to_liters(gallon_sample)
    
    m3_value = cubic_meters_to_liters(0.264172052358148 * gallon_sample / METER_TO_LITERS_FACTOR) # Indirect calc for sanity check or just convert L to m3
    
    liters_per_cubic_meter_inv = 1/METER_TO_LITERS_FACTOR
    c_m_from_l = l_from_gal * liters_per_cubic_meter_inv
    
    print(f"{l_from_gal:.4f} Liters")
    print("{:.9f} m³".format(c_m_from_l))

if __name__ == '__main__':
    main()