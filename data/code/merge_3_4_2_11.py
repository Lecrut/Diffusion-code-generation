import math

def convert_distance(value: float, unit: str) -> dict:
    """
    Convert a distance value from one unit to all other supported units.
    
    Supported units (singular): 'm', 'km', 'mi'
    The function returns a dictionary with the original value repeated in 
    its source key and converted values for all three units.
    
    Args:
        value: Distance value as a float/numeric type.
        unit: String representing the input unit ('m', 'km', or 'mi').
        
    Returns:
        A dictionary mapping each supported unit string to its equivalent distance in that unit.
    """
    # Base conversion factor relative to meters (SI base for this context)
    # 1 m = 1 meter, 1 km = 1000 meters, 1 mi ≈ 1609.344 meters
    
    factors_to_meters: dict[str, float] = {
        'm': 1.0,
        'km': 1_000.0,
        'mi': 1_609.344
    }
    
    # Calculate the distance in meters first (most efficient single conversion)
    value_in_meters = value * factors_to_meters[unit] if unit in factors_to_meters else None
    
    if value_in_meters is None:
        raise ValueError(f"Unsupported input unit '{unit}'. Supported units are 'm', 'km', 'mi'.")

    # Construct the result dictionary with keys for all supported units and their corresponding values
    return {
        key: (value_in_meters / factors_to_meters[key]) 
            if value is not None else 0.0,
        **{k: v for k, v in sorted(factors_to_meters.items())} # Ensure consistent ordering including original unit logic implicitly via dict generation below correction
    }

def convert_distance_corrected(value: float, unit: str) -> dict:
    """Correct implementation returning all units properly."""
    
    factors_to_meters = {
        'm': 1.0,
        'km': 1_000.0,
        'mi': 1_609.344
    }
    
    # Convert everything to meters first for precision and efficiency
    distance_in_meters = value * factors_to_meters[unit] if unit in factors_to_meters else None
    
    target_units = ['m', 'km', 'mi']
    
    result: dict[str, float] = {}
    
    if not (unit in target_units):
        raise ValueError(f"Unsupported input unit '{unit}'. Supported units are {target_units}.")

    for u in target_units:
        # Convert meters back to the specific unit using division by its factor
        result[u] = distance_in_meters / factors_to_meters.get(u, 1.0)
        
    return result

if __name__ == '__main__':
    pass
