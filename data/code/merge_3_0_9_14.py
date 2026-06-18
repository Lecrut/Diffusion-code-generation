import math

# Supported units: m, km, cm, mm, um (micrometer), nm (nanometer)
UNIT_TO_METER = {
    'm': 1,
    'km': 10**3,
    'cm': 1e-2,
    'mm': 1e-3,
    'um': 1e-6,
    'nm': 1e-9,
}

def convert_length(value: float, source_unit: str, target_unit: str) -> float:
    """
    Convert a length from one supported unit to another.
    
    Args:
        value (float): The length in the source unit.
        source_unit (str): Source unit string ('m', 'km', 'cm', 'mm', 'um', 'nm').
        target_unit (str): Target unit string ('m', 'km', 'cm', 'mm', 'um', 'nm').

    Returns:
        float: The converted length in the target unit.

    Raises:
        ValueError: If unsupported units are provided or conversion is invalid.
    """
    if source_unit not in UNIT_TO_METER:
        raise ValueError(f"Unsupported source unit: {source_unit}. Supported units: m, km, cm, mm, um, nm.")
    
    target_unit = str(target_unit).strip().lower()
    if target_unit not in UNIT_TO_METER:
        raise ValueError(f"Unsupported target unit: {target_unit}. Supported units: m, km, cm, mm, um, nm.")

    meters = value * UNIT_TO_METER[source_unit]
    return meters / UNIT_TO_METER[target_unit]

if __name__ == '__main__':
    # Sample conversions without interactive input
    
    test_cases = [
        (100.5, 'cm', 'm'),          # 1 meter -> expected: ~1.005 m
        (2.3, 'km', 'mm'),           # 2.3 km -> expected: 2_300_000 mm
        (5e-6, 'um', 'nm'),          # 5 um -> expected: 5000 nm
        (1/4, 'm', 'cm'),            # 0.25 m -> expected: 25 cm
    ]

    print("Length Conversion Results:\n")
    for val, src, tgt in test_cases:
        result = convert_length(val, src, tgt)
        print(f"{val} {src} is equivalent to {result:.6f} {tgt}")