import math

def validate_duration(value: float) -> bool:
    """Check if a duration value is non-negative."""
    return isinstance(value, (int, float)) and value >= 0

def convert_to_units(seconds: float) -> dict:
    """Convert seconds to minutes, hours, days, and weeks."""
    result = {}
    
    # Calculate values with appropriate precision for display
    if seconds < 60:
        result['minutes'] = round(seconds / 60, 2)
    else:
        result['minutes'] = round(seconds / 60, 4)
        
    hours_total = seconds / 3600.0
    
    # Check for significant digits in hours to avoid excessive decimals unless it's a whole number or close to one
    if abs(hours_total - round(hours_total)) < 1e-9:
        result['hours'] = int(round(hours_total))
    else:
        result['hours'] = round(hours_total, 2)
        
    days_total = seconds / 86400.0
    
    # Check for significant digits in days to avoid excessive decimals unless it's a whole number or close to one
    if abs(days_total - round(days_total)) < 1e-9:
        result['days'] = int(round(days_total))
    else:
        result['days'] = round(days_total, 2)
        
    weeks_total = seconds / (7 * 86400.0)
    
    # Check for significant digits in weeks to avoid excessive decimals unless it's a whole number or close to one
    if abs(weeks_total - round(weeks_total)) < 1e-9:
        result['weeks'] = int(round(weeks_total))
    else:
        result['weeks'] = round(weeks_total, 2)
        
    return result

def convert_from_unit(value: float, unit: str) -> dict:
    """Convert a given duration from a specific unit to all other standard units."""
    
    # Validate input value
    if not validate_duration(value):
        raise ValueError(f"Duration must be non-negative. Received: {value}")
        
    # Map valid units and their conversion factors to seconds
    unit_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 7 * 86400
    }
    
    # Validate input unit
    if unit.lower() not in unit_factors:
        raise ValueError(f"Unsupported time unit. Valid units are: seconds, minutes, hours, days, weeks")
        
    factor = unit_factors[unit.lower()]
    total_seconds = value * factor
    
    return convert_to_units(total_seconds)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_cases = [
        {'value': 3600, 'unit': 'seconds'},      # Should result in exactly 1 hour
        {'value': 45.5, 'unit': 'minutes'},       # Mixed unit conversion
        {'value': 2.75, 'unit': 'hours'},         # Fractional hours to days/weeks
        {'value': 30, 'unit': 'days'},            # Large duration
        {'value': 14, 'unit': 'weeks'}             # Very large duration (exactly 98 days)
    ]
    
    print("Time Unit Conversion Results:")
    print("-" * 50)
    
    for test in test_cases:
        value = float(test['value'])
        unit = test['unit']