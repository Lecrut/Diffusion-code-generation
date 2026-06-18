"""Volume management module for converting between metric and imperial units."""

from typing import Union

class VolumeError(Exception):
    """Custom exception raised for invalid volume conversions or types."""

    pass

# Conversion factors relative to cubic meters (m³)
METRIC_TO_CUBIC_METERS: dict[str, float] = {
    "L": 0.001,
    "m3": 1.0,
}

IMPERIAL_TO_LITERS: dict[str, float] = {
    "gal": 3.785411784,
    "qt": 0.946352946,
    "pt": 0.473176473,
}

IMPERIAL_TO_CUBIC_METERS: dict[str, float] = {
    "gal": 3.785411784e-3,
    "qt": 9.46352946e-4,
    "pt": 4.73176473e-4,
}

LITERS_TO_CUBIC_METERS = {k: v * METRIC_TO_CUBIC_METERS[k] for k, v in IMPERIAL_TO_LITERS.items()}

def _validate_input(input_volume: Union[int, float], input_unit: str) -> None:
    """Validate the type and unit of the provided volume."""
    if not isinstance(input_volume, (int, float)):
        raise VolumeError(f"Volume must be a number, got {type(input_volume).__name__}")

    valid_units = [k for k in METRIC_TO_CUBIC_METERS.keys() + IMPERIAL_TO_LITERS.keys()]
    if input_unit.lower().strip() not in valid_units:
        raise VolumeError(f"Invalid unit '{input_unit}'. Valid units are {valid_units}.")

def to_cubic_meters(volume_in_liters_or_gal: Union[int, float], unit: str) -> float:
    """Convert any volume (L or gal) to cubic meters.

    Args:
        volume_in_liters_or_gal: The input numeric value.
        unit: The unit of the input ('L', 'l', 'm3', 'gal', etc.).

    Returns:
        The equivalent volume in cubic meters (float).

    Raises:
        VolumeError: If inputs are invalid or unsupported units provided.
    """
    _validate_input(volume_in_liters_or_gal, unit)

    normalized_unit = unit.lower().strip()
    
    if normalized_unit == "m3":
        return float(volume_in_liters_or_gal) * METRIC_TO_CUBIC_METERS["m3"]
    
    # Convert to liters first (if metric), then to cubic meters
    lit_value: Union[int, float] = volume_in_liters_or_gal
    
    if normalized_unit in ["l", "ml"]:
        if normalized_unit == "ml":
            lit_value *= 0.001
        
        return lit_value * METRIC_TO_CUBIC_METERS["L"]

    # Convert gallons to liters, then cubic meters using the derived factor
    gal_to_lit_factor = IMPERIAL_TO_LITERS.get(normalized_unit)
    
    if not gal_to_lit_factor:
        raise VolumeError(f"Unsupported imperial unit '{normalized_unit}'")
        
    lit_value *= gal_to_lit_factor
    
    return lit_value * METRIC_TO_CUBIC_METERS["L"]

def to_cubic_meters_from_input(volume_val: Union[int, float], volume_str: str) -> float:
    """Convenience wrapper for converting any input unit to cubic meters.

    This function handles both metric (Liters/mL/cubic meters) and Imperial units directly.

    Args:
        volume_val: The numeric value of the volume.
        volume_str: String representation of the unit ('L', 'm3', 'gal' etc).

    Returns:
        Volume in cubic meters.

    Raises:
        VolumeError: If inputs are invalid or unsupported units provided.
    """
    return to_cubic_meters(volume_val, volume_str)

def convert_to_metric_liters(input_volume: Union[int, float], input_unit: str) -> float:
    """Convert any unit (metric or imperial) to liters.

    Args:
        input_volume: The numeric value of the volume.
        input_unit: String representing the current unit ('L', 'm3', 'gal').

    Returns:
        Equivalent volume in liters as a float.

    Raises:
        VolumeError: If inputs are invalid or unsupported units provided.
    """
    _validate_input(input_volume, input_unit)
    
    normalized = input_unit.lower().strip()
    
    if normalized == "m3":
        return input_volume * 1000
    
    # Metric to Liters (already in base mostly)
    if normalized in ["l", "ml"]:
        val: float = input_volume
        if normalized == "ml":
            val *= 1000.0
            
        return val

    # Imperial conversion factor to liters
    gal_to_lit_factor = IMPERIAL_TO_LITERS.get(normalized)
    
    if not gal_to_lit_factor:
        raise VolumeError(f"Unsupported imperial unit '{normalized}'")
        
    return input_volume * gal_to_lit_factor

def convert_to_imperial_gallons(input_volume: Union[int, float], input_unit: str) -> float:
    """Convert any metric or imperial volume to gallons.

    Args:
        input_volume: The numeric value of the volume.
        input_unit: String representing current unit ('L', 'm3', 'gal').

    Returns:
        Equivalent volume in US gallons as a float (default for "gal").

    Raises:
        VolumeError: If inputs are invalid or unsupported units provided.
    """
    _validate_input(input_volume, input_unit)
    
    normalized = input_unit.lower().strip()

    # Convert to cubic meters first if necessary, then back up the chain (m3 -> gal) OR direct conversion
    
    if normalized == "gal":
        return float(input_volume)
        
    # Metric: m3 or L -> gallons via liters factor and base volume in cubics
    lit_val = convert_to_metric_liters(input_volume, input_unit)

    # Gallons to Liters ratio is 1/0.264172052 (approx), but better calculate directly from constants:
    
    gal_factor_from_liters = IMPERIAL_TO_LITERS["gal"] ** -1
    
    return lit_val * gal_factor_from_liters

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without user input.

    samples_metric_to_imperial: list[dict] = [
        {"input_value": 5, "input_unit": "L", "expected_desc": "Convert L to gal"},
        {"input_value": 100, "input_unit": "m3", "expected_desc": "Convert m3 to gal"},
        {"input_value": 24.75, "input_unit": "gal", "expected_desc": "Verify input already in gal (identity)"},
    ]

    samples_imperial_to_metric: list[dict] = [
        {"input_value": 10, "input_unit": "gal", "expected_desc": "Convert gal to L"},
        {"input_value": 5.924, "input_unit": "qt", "expected_desc": "Convert qt to L"},
    ]

    print("=== Volume Conversion Tests ===\n")

    # Metric -> Imperial (Liters/Gallons) conversion examples
    for sample in samples_metric_to_imperial:
        val = sample["input_value"]
        unit = sample["input_unit"]
        
        if "gal" in unit.lower():
            gallons_out = convert_to_imperial_gallons(val, unit)
            print(f"{val} {unit.upper()} -> ~{gallons_out:.3f} US Gallon")

    # Imperial -> Metric conversion examples (Gallons/Liters)
    for sample in samples_imperial_to_metric:
        val = sample["input_value"]
        unit = sample["input_unit"]
        
        liters_out = convert_to_metric_liters(val, unit)
        print(f"{val} {unit.upper()} -> ~{liters_out:.3f} Liters")

    # Additional specific test