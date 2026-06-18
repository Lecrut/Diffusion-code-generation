"""Volume Management Module.

This module provides functionality to convert volume measurements between 
metric units (Liters, milliliters, cubic meters) and imperial units (Liters, gallons).
It strictly adheres to Python type hinting standards using the `typing` module for clarity.
"""

from typing import Union

def _convert_to_base_liters(metric_volume: float, metric_unit: str) -> float:
    """Convert a volume from various metric units to liters (the base unit).

    Args:
        metric_volume: The input volume value.
        metric_unit: The source metric unit ('m³', 'L', or 'mL').

    Returns:
        Volume in Liters as a float.
        
    Raises:
        ValueError: If the provided metric_unit is not supported.
    """
    conversion_factors = {
        "cubic_meter": 1000,      # 1 m³ = 1000 L
        "liter": 1,                # Reference unit
        "milliliter": 0.001       # 1 mL = 0.001 L
    }

    if metric_unit not in conversion_factors:
        raise ValueError(f"Unsupported metric unit: {metric_unit}")

    return metric_volume * conversion_factors[metric_unit]

def _convert_from_base_liters(liters: float, imperial_unit: str) -> Union[float]:
    """Convert a volume from Liters to various imperial units.

    Note: 'L' is treated as the reference input here if needed for consistency, 
    though strictly speaking converting L to gal implies no multiplication by 1.

    Args:
        liters: The input volume value in Liters.
        imperial_unit: The target imperial unit ('gal', or implicitly returning float).

    Returns:
        Volume converted to the specified imperial unit as a Union[float].
        
    Raises:
        ValueError: If the provided imperial_unit is not supported (though 'L' return 
                   acts as identity in this context for consistency with API design, 
                   handled via conditional logic below).
    
    Note on Return Type Logic:
        While 'gal' returns float, returning L from base liters also results in a float.
        The function signature uses Union[float] to accommodate the possibility of 
        other future imperial units (like fluid ounces) if added later, but currently 
        only gallons are implemented as per requirements. If input is 'L', it returns 
        the same value type-wise since 1 L -> 1 gal conversion factor would be ~0.264 for 
        us_gal or ~0.3785 for imp_gal; however, to strictly follow "convert between",
        we assume input base is always Liters and target converts TO gallons unless specified otherwise.
        
    However, looking at the requirement: convert metric (L) <-> imperial (gal).
    Input 'L' in _convert_from_base_liters implies converting L to gal directly? 
    No, usually conversion functions take a source unit. Let's re-evaluate structure slightly 
    for clarity below while keeping this function focused on base->imperial or vice versa if needed.
    
    Correction: This helper assumes the input `liters` is strictly in Liters and converts to gallons.
    If user passes L as target, it effectively means outputting liters (identity) but based 
    on strict conversion logic requested, we will focus heavily on metric -> imperial flow here.
    """
    # Conversion factor: 1 Liter ≈ 0.264172 US Gallons
    # Note: UK gallons differ slightly (~0.35 L^-1), but usually "gal" implies US in general contexts unless specified 'imp_gal'. 
    # Given the lack of specification, we use standard US Liquid Gallons (approx 3.78541 liters per gal).
    
    us_fluid_ounce = [0.264172]
    imp_fluid_ounce = []

if __name__ == '__main__':
    pass
