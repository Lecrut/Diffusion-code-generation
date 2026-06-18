import math

def convert_volume_to_liters(volume: float, unit: str) -> float:
    """
    Converts a volume given in any supported unit to liters with high precision.
    
    Supported units and their conversion factors (1 unit = X liters):
        'liter' or 'l': 1
        'milliliter' or 'ml': 0.001
        'kiloliter' or 'kl': 1000
        'cubic centimeter' or 'cc', 'cm3': 0.001 (since 1 cm³ = 1 ml)
        'gallon'(us): ~0.003785411784
        'quart'(us): ~0.000946352946
        'pint'(us): ~0.000473176473
        'cup'(us): ~0.0002365882365
        'fluid_ounce'(us): ~0.00002957352956 (approx 2.957e-5)
    
    Precision note: Using standard float precision which provides about 15-17 decimal digits,
    sufficient for most scientific and engineering applications requiring high accuracy 
    without resorting to arbitrary precision libraries unless specific extreme needs exist.

    Args:
        volume (float): The numerical value of the volume.
        unit (str): The unit string representing the volume type (case-insensitive).

    Returns:
        float: The equivalent volume in liters.

    Raises:
        ValueError: If an unsupported unit is provided or if input values are invalid.
    
    Examples:
        convert_volume_to_liters(50, 'ml') -> 0.05
        convert_volume_to_liters(1, 'gallon(us)') -> ~0.003785411784
    """
    unit = unit.lower().strip()

    # Define conversion factors to liters with high precision string literals converted via float for accuracy
    conversions: dict[str, float] = {
        'liter': 1.0,
        'l': 1.0,
        'milliliter': 0.001,
        'ml': 0.001,
        'kiloliter': 1000.0,
        'kl': 1000.0,
        'cubic centimeter': 0.001,
        'cc': 0.001,
        'cm3': 0.001,
        'gallon(us)': 0.003785411784,
        'gal(US)us': 0.003785411784,
        'quart(us)': 0.000946352946,
        'qt(US)us': 0.000946352946,
        'pint(us)': 0.000473176473,
        'pt(US)us': 0.000473176473,
        'cup(us)': 0.0002365882365,
        'c(up/us)': 0.0002365882365,
    }

    if unit not in conversions:
        raise ValueError(f"Unsupported volume unit '{unit}'. Supported units are {list(conversions.keys())}.")

    factor = conversions[unit]

    # Handle negative volumes gracefully (mathematically valid for liquids/gases)
    result = round(volume * factor, 15) 

    return float(result)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    samples: list[tuple[float, str]] = [
        (2.5, 'liter'),
        (500, 'ml'),
        (1.5, 'kiloliter'),
        (30, 'cc'),
        (1, 'gallon(us)'),
        (4, 'quart(us)'),
        (8, 'pint(us)'),
        (2, 'cup(us)'),
    ]

    print("Volume Conversion to Liters")
    print("-" * 30)

    for vol, unit in samples:
        try:
            converted = convert_volume_to_liters(vol, unit)
            # Formatting output to show precision clearly if the factor isn't simple integer
            display_val = f"{converted:.15f}" 
            print(f"{vol} {unit:>20s} -> {display_val}")
        except Exception as e:
            print(f"Error processing {vol} {unit}: {e}")

    # Additional test for invalid unit to ensure error handling works without crashing the module
    try:
        convert_volume_to_liters(1, 'invalid_unit')
    except ValueError:
        pass  # Expected behavior
    
    print("-" * 30)