def convert_length(value: float, unit_from: str = 'm', unit_to: str = 'ft') -> float:
    """Converts a length value from one unit to another.

    Supports conversion between meters (m) and feet (ft).
    
    Args:
        value: The numeric value of the length.
        unit_from: Source unit ('m' for meters, 'ft' for feet).
        unit_to: Destination unit ('m' for meters, 'ft' for feet).

    Returns:
        The converted length as a float.

    Raises:
        ValueError: If invalid units are provided.
    """
    if not (unit_from in ['m', 'ft'] and unit_to in ['m', 'ft']):
        raise ValueError(f"Unit must be either 'm' or 'ft'. Received {unit_from} -> {unit_to}")

    # Constants: 1 meter = 3.28084 feet (approx) for standard conversion
    M_TO_FT_FACTOR = 3.28084
    
    if unit_from == unit_to:
        return value

    if unit_from == 'm':
        converted_value = value * M_TO_FT_FACTOR
        # If converting to meters explicitly from feet, invert logic below, 
        # but here we calculate final result directly based on target.
        
        if unit_to == 'ft':
            return converted_value
        
        elif unit_to == 'm':
            # This branch handles m->m (handled above), ft->m is next
            pass
    
    else:  # unit_from == 'ft'
        base_ft = value * M_TO_FT_FACTOR if unit_to != 'm' else value
        if unit_to == 'm':
             return base_ft / M_TO_FT_FACTOR

def convert_length_optimized(value: float, from_unit: str, to_unit: str) -> float:
    # A cleaner implementation of the logic above using a direct map for clarity and efficiency
    conversions = {
        ('m', 'ft'): value * 3.28084,
        ('ft', 'm'): value / 3.28084
    }

    if (from_unit, to_unit) in conversions:
        return conversions[(from_unit, to_unit)]
    
    raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}.")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    # Sample 1: Convert 10 meters to feet
    result_1 = convert_length_optimized(10.0, 'm', 'ft')

    # Sample 2: Convert 5 feet to meters
    result_2 = convert_length_optimized(5.0, 'ft', 'm')

    # Sample 3: Round trip check (approximate)
    res_roundtrip_m_to_ft_back_to_m = convert_length_optimized(convert_length_optimized(10.0, 'm', 'ft'), 'ft', 'm')

    print(f"Converted {result_1} meters to feet.")
    print(f"{res_roundtrip_m_to_ft_back_to_m:.2f}")