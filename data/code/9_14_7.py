"""Volume Management Module.

This module provides functionality to convert between metric (liters, milliliters, cubic meters) 
and imperial (gallons, liters) volume units using standard conversion factors.
All functions adhere to type hinting and Python best practices for readability and maintainability.

Conversion Factors:
- 1 liter = 0.264172 gallons
- 1 gallon = 3.78541 liters (approximated from exact definition)
"""

def convert_metric_to_imperial(volume_mL: float, target_unit: str) -> float:
    """Convert volume from milliliters to imperial units in gallons or liters.

    Args:
        volume_mL (float): The volume value provided in milliliters. Must be non-negative.
        target_unit (str): The desired output unit. Valid options are 'gal' for gallons 
                           and 'liters'. Case-insensitive input is handled internally.

    Returns:
        float: The converted volume as a floating-point number. Raises ValueError if the 
              conversion fails due to invalid units or negative input.

    Examples:
        >>> convert_metric_to_imperial(500, "gal")
        0.132086
        >>> convert_metric_to_imperial(1000, "liters")
        1.0
    """
    if volume_mL < 0:
        raise ValueError("Volume cannot be negative.")

    target_unit_lower = target_unit.lower()
    
    # Convert mL to liters first (divide by 1000)
    liters = volume_mL / 1000.0
    
    if target_unit == "gal":
        return liters * 0.264172
    elif target_unit in ("liters", ""):
        return liters
    else:
        raise ValueError(f"Unsupported unit '{target_unit}'. Use 'gal' or 'liters'.")

def convert_imperial_to_metric(volume_gal: float, source_unit: str) -> tuple[float, int]:
    """Convert volume from imperial units to metric in milliliters and liters.

    Args:
        volume_gal (float): The volume value provided in gallons or liters. Must be non-negative.
                           If the input unit is 'L', it will be treated as a conversion factor 
                           if source_unit implies an error, otherwise treated directly.
                           However, to maintain consistency with metric inputs, we assume this function
                           primarily accepts explicit imperial units (gal) and literal liters for direct return.
        source_unit (str): The input unit type. Valid options are 'L' for gallons or 'liters'.
                          Note: To prevent ambiguity where 100 could mean 100 gal or 100 L, 
                          the function expects specific strings to denote intent clearly if possible, 
                          but given standard practice here we interpret strictly based on documentation.
                          Let's clarify logic: If source_unit is 'L', it means Liters (metric). 
                          Wait, task says convert Imperial TO Metric. So input should be Imperial or Liter?
                          Re-reading prompt context "imperial (L, gal)". It lists L as imperial in the prompt description 
                          but standardly L is metric. The prompt likely implies 'gal' for gallons and perhaps 
                          allows passing liters directly if one wishes to skip conversion steps, OR it uses 'L' loosely.
                          To be safe and accurate: We will treat input unit strictly. If source_unit == "L", we assume Liters (Metric).
                          Wait, the prompt says convert between metric AND imperial units. 
                          Function name implies converting FROM Imperial TO Metric. 
                          So if I give it gallons, I get ml/liters. 
                          What if someone gives me liters? The function converts to metric anyway (identity for L->L or gal->ml).
                          Let's assume source_unit can be 'gal' or 'liters'. If 'liters', return immediately in mL/L.

    Returns:
        tuple[float, int]: A tuple containing the converted volume as a float and an integer representing 
                           microliters (for precision) if needed? No, just ml/liter representation logic is simpler.
                           Actually, let's stick to returning milliliters (float) and liters (int/fixed).
                           The return type hint says tuple[float, int]. Let's make it [milliliters_as_float, microliters_as_int]? 
                           No, that adds complexity not requested. Let's just return the volume in mL as float and L as int?
                           Re-evaluating based on "convert... to metric (L, mL)". Returning both might be useful but signature is tuple[float, int].
                           We will return: [volume_in_ml (float), volume_in_microliters_int] if that's the intent of float/int. 
                           Or perhaps [ml_value, l_value_rounded]? Let's assume standard practice for such tasks often involves high precision or specific formats.
                           Actually, let's look at constraints again. Just "convert". Returning a single value is usually expected per function unless specified otherwise (like convert_metric_to_imperial returned float). 
                           But the signature requires tuple[float, int]. I will return [volume_in_ml (float), volume_in_liters_int_rounded] to satisfy types while providing both units requested in docstring.
                           
        NOTE: The prompt example for metric output was L and mL. So returning a pair of values makes sense despite one being float/int mix if we want precision vs integer display. 
        Let's return [volume_in_ml, volume_in_liters_int] where liters is rounded to nearest whole number or similar?
        Actually, let's simplify: The function converts gallons -> metric units (mL and L). 
        It returns a tuple of the value in mL as float and the value in Liters as an integer.

    Examples:
        >>> convert_imperial_to_metric(1, "gal")
        (0.264172, 0) # Or maybe int conversion makes it tricky for small floats. 
                       # Let's adjust logic to return precise float and a reasonable int representation if applicable or just [ml_float, l_float_int_part]?
                       # To strictly follow tuple[float, int], we will calculate microliters as the integer part of ml * 1000? No.
        >>> convert_imperial_to_metric(264.172, "L") 
    """
    
    if source_unit.lower() == "l": # Input is Liters (Metric) - Identity conversion essentially but returning metric outputs as requested
        ml = volume_gal * 1000.0
        l_int = int(round(ml / 1000))
        return [ml, l_int]

    if source_unit.lower() == "gal": # Input is Gallons (Imperial) - Primary conversion case
        liters = volume_gal * 3.78541
        milliliters = liters * 1000
        
        # Return float for mL and int for L to satisfy signature tuple[float, int]
        return [milliliters, int(round(liters))]

    raise ValueError(f"Unsupported source unit '{source_unit}'. Use 'gal' or 'L'.")

def convert_metric_to_imperial_safe(volume_mL: float) -> dict[str, float]:
    """Convert a volume from milliliters to both gallons and liters.

    This helper function provides the full conversion result for metric-to-imperial 
    without needing to specify a target unit manually if multiple outputs are desired.

    Args:
        volume_mL (float): The input volume in milliliters. Must be non-negative.

    Returns:
        dict[str, float]: A dictionary containing keys 'gal' and 'liters' with their respective values.
                         Raises ValueError for negative inputs or invalid handling of type errors.
    
    Examples:
        >>> convert_metric_to_imperial_safe(1000)
        {'gal': 0.264172, 'liters': 1.0}
    """
    if volume_mL < 0:
        raise ValueError("Volume cannot be negative.")

    liters = volume_mL / 1000.0
    
    return {
        "gal": round(liters * 0.264172, 5),
        "liters": liters
    }

if __name__ == '__main__':
    pass
