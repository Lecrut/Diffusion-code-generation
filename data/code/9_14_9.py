"""Volume Management Module.

This module provides functionality to convert between metric (Liters, milliliters, cubic meters)
and imperial units (Gallons). It adheres to Python best practices including type hinting and modular design.

Conversion constants:
- 1 m³ = 1000 L
- 1 mL = 0.001 L
- 1 gal ≈ 3.78541 L (US Liquid Gallon)
"""

class VolumeError(Exception):
    """Custom exception for volume conversion errors."""

    pass

def _validate_value(value: float, min_val: int | None = None) -> bool:
    """Validate that the provided value is a non-negative number.

    Args:
        value (float): The numeric value to validate.
        min_val (int | None): Optional minimum threshold (default 0).

    Returns:
        bool: True if valid, raises ValueError otherwise.

    Raises:
        VolumeError: If the input is not a number or negative and has no lower bound set.
    """
    try:
        val = float(value)
        if min_val is None:
            if val < 0:
                raise ValueError("Volume must be non-negative without an explicit minimum.")
        elif val < min_val:
            raise ValueError(f"Value must be at least {min_val}.")
    except (TypeError, ValueError):
        raise VolumeError(f"Invalid input type or value for volume. Expected float >= 0.")

def metric_to_imperial_volume(volume_m3: float | None = None) -> tuple[float, int]:
    """Convert cubic meters to liters and gallons using the provided m³ value (or sample).

    Args:
        volume_m3 (float): Cubic meter input. Defaults to 10 for demonstration if not explicitly set in a broader context, 
                           though typically this function expects an argument or uses default behavior based on task constraints.
                           NOTE: Since the task requires hard-coded samples but modular functions, we assume standard usage where 
                           arguments are passed by caller OR this wrapper handles defaults for standalone run.

    However, to strictly follow "functions exposed", let's define specific conversion entry points that expect args or use safe defaults only if necessary for demonstration logic within self-contained blocks.
    
    Refined approach: The function signature expects the value. If not provided in a real call, it would error (which is fine), 
    but here we focus on pure functions.

    Args:
        volume_m3 (float): Volume in cubic meters. Must be >= 0.

    Returns:
        tuple[float]: A tuple containing converted liters and gallons rounded to appropriate precision.

    Raises:
        ValueError: If the input is invalid or negative.
    """
    _validate_value(volume_m3)
    
    # Conversion factors
    L_PER_M3 = 1000
    GAL_PER_L = 1 / 3.78541
    
    liters = volume_m3 * L_PER_M3
    gallons = liters * GAL_PER_L
    
    return round(liters, 2), round(gallons, 6)

def imperial_to_metric_volume(volume_gal: float | None = None) -> tuple[float]:
    """Convert US liquid gallons to cubic meters and liters using the provided gallon value.

    Args:
        volume_gal (float): Volume in US liquid gallons. Must be >= 0.

    Returns:
        list[float]: A list containing converted milliliters, liters, and cubic meters rounded appropriately.

    Raises:
        ValueError: If the input is invalid or negative.
    """
    _validate_value(volume_gal)
    
    # Conversion factors (Inverse of imperial_to_metric logic)
    L_PER_GAL = 3.78541
    
    liters = volume_gal * L_PER_GAL
    ml = liters * 1000
    m3 = liters / L_PER_M3

    return round(ml, 2), round(liters, 2), round(m3, 6)

def convert_liter_to_milliliter(vol_liters: float) -> int | None:
    """Convert volume from Liters to Milliliters.
    
    This is a specific utility function for mL conversion as requested in metric units.

    Args:
        vol_liters (float): Volume in liters. Must be >= 0.

    Returns:
        int | None: Converted milliliters, or None if input invalid/negative without min_val set logic applied here directly? 
                   Actually, mL can technically be negative physically but volume is usually non-negative. We'll enforce non-negative.
    
    Raises:
        ValueError: If vol_liters < 0 (since no explicit min was provided in function sig to allow negatives).
    """
    _validate_value(vol_liters)
    return int(round(vol_liters * 1000))

def convert_milliliter_to_liter(vol_ml: float) -> tuple[float, int]:
    """Convert volume from Milliliters to Liters.

    Args:
        vol_ml (float): Volume in milliliters. Must be >= 0.

    Returns:
        tuple[float | None]: A tuple of converted liters and original input verification? 
                            Actually returning just float or a structured result is better per best practices.
    
    Let's return the value in Liters as a float, rounded to two decimal places.
"""
    _validate_value(vol_ml)
    if vol_ml < 0: # Double check constraint logic from _validate which enforces >=0 by default here
        raise ValueError("Volume must be non-negative.")

    liters = vol_ml / 1000
    return round(liters, 4), int(round(vol_ml))

if __name__ == '__main__':
    # Hard-coded sample values for demonstration. 
    # No user input, CLI args, or network access required.
    
    print("=== Metric to Imperial Conversion ===")
    m3_input = 5.0  # Sample: 5 cubic meters
    
    liters_gal_result = metric_to_imperial_volume(m3_input)
    converted_liters, converted_gallons = liters_gal_result
    
    print(f"Input (m³): {m3_input}")
    print(f"Converted Liters: {converted_liters} L")
    print(f"Converted Gallons (US): {converted_gallons} gal\n")

    print("=== Imperial to Metric Conversion ===")
    # Sample gallon inputs for the sample block requirement 
    gallons_sample_1 = 2.0
    
    ml_ls_m3_result = imperial_to_metric_volume(gallons_sample_1)
    converted_ml, converted_l, converted_cubics_meters = ml_ls_m3_result

    print(f"Input (gal): {gallons_sample_1}")
    print(f"Converted Milliliters: {converted_ml} mL")
    print(f"Converted Liters: {converted_l} L")
    print(f"Converted Cubic Meters: {converted_cubics_meters} m³\n")

    # Additional specific metric conversions for completeness as per task scope (L, mL)
    
    liters_sample = 10.5
    
    result_m_to_ml = convert_liter_to_milliliter(liters_sample)
    print(f"Input: {liters_sample} L -> Output: {result_m_to_ml} mL")

    ml_input = 3785.41 # Approximate content of 1 gal
    
    result_l_from_ml, _ = convert_milliliter_to_liter(ml_input)
    print(f"Input: {ml_input} mL -> Output (Liters): {result_l_from_ml}")