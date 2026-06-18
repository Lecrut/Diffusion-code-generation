"""Unit conversion module supporting Metric to Imperial and vice versa."""

def convert_length(value: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
    """Convert a length value between metric and imperial units.
    
    Supported units: 'm', 'cm', 'km' (metric); 'ft', 'in', 'yd', 'mi' (imperial).
    
    Args:
        value: The numeric value to convert.
        from_unit: Source unit string ('m', 'cm', 'km', 'ft', 'in', 'yd', 'mi').
        to_unit: Target unit string ('m', 'cm', 'km', 'ft', 'in', 'yd', 'mi').
        
    Returns:
        A tuple containing the converted float value and a dictionary of factors used.
    
    Raises:
        ValueError: If unsupported units are provided or conversion is invalid.
    """
    # Define base values relative to meters for metric, 
    # relative to feet/centimeters depending on mix. Simplified strategy:
    # Convert everything first to standard SI (meters), then to target.
    
    if from_unit.lower() in ('km', 'cm') and to_unit == from_unit.lower():
        return value, {"factors": {}}

    unit_factors_to_m = {'m': 1.0, 'km': 1e-3, 'cm': 1e2}
    # For imperial, use feet as intermediate reference for consistency with meters in one step? 
    # Actually simpler: convert everything to a common base (Meters or Feet), then to target.
    
    unit_factors_from_m = {'m': 1.0, 'km': 1e3, 'cm': 1e-2}
    
    imperial_base_to_meter_factor = {
        'ft': 0.3048, 
        'in': 0.0254, 
        'yd': 0.9144, 
        'mi': 1609.344 # meters per mile (approx)
    }

    if from_unit.lower() not in ('m', 'cm', 'km') and to_unit.upper() == 'METRIC':
        raise ValueError("Cannot directly convert Imperial metric without intermediate step.")

    
    unit_lower = from_unit.lower().strip()
    target_metric_base = {'ft': 0.3048, 'in': 0.3048/12, 'yd': 0.9144, 'mi': 1609.344} # m per unit

    
    if from_unit.lower() in ('m', 'cm', 'km'):
        meters = value * ( {'m': 1, 'cm': 0.01, 'km': 1000}[unit_lower] ) 
        result_meters = value * ( {'m': 1, 'cm': 0.01, 'km': 1000} or 1 )[from_unit.lower()]
        
    # Re-implementation for clarity
    
    base_metric_vals_to_factor_from_1m = {
        "ft": 3.28084, 
        "in": 39.3701, 
        "yd": 3.28084 * 3, 
        "mi": 5280 * 3.28084 # roughly
    }

if __name__ == '__main__':
    pass
