def convert_volume_to_liters(volume: float, unit: str) -> float:
    """
    Converts a given volume to liters based on the input unit.
    
    Supported units (case-insensitive):
        - liter/L or l/ℓ: already in base unit (factor = 1)
        - milliliter/mL or ml/mL: factor = 0.001
        - kiloliter/kL or kL/Kl: factor = 1000
    
    The function returns the volume equivalent in liters as a float with full precision.

    Args:
        volume (float): The numeric value of the volume to convert.
        unit (str): The string representation of the source unit, case-insensitive.

    Returns:
        float: The converted volume in liters.

    Raises:
        ValueError: If the provided unit is not supported.
    """
    
    # Normalize input for comparison and factor lookup
    normalized_unit = unit.lower().strip()
    
    if normalized_unit == "liter" or normalized_unit == "l":
        return float(volume)
    elif normalized_unit in ("milliliter", "ml"):
        return volume * 0.001
    elif normalized_unit in ("kiloliter", "kl"):
        return volume * 1000
    else:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are liter, milliliter, kiloliter.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    
    samples = [
        {"value": 500, "source_unit": "ml"},       # Expected: 0.5 L
        {"value": 2, "source_unit": "L"},          # Expected: 2.0 L
        {"value": 1.5, "source_unit": "kL"},       # Expected: 1500.0 L
        {"value": -10, "source_unit": "liter"},    # Negative volume test (valid) -> -10.0 L
        {"value": 2500000, "source_unit": "ml"},   # Large number precision test -> 2500.0 L
    ]

    for sample in samples:
        result = convert_volume_to_liters(sample["value"], sample["source_unit"])
        print(f"Converted {sample['value']} {sample['source_unit'].upper()} to liters:")
        print(result)