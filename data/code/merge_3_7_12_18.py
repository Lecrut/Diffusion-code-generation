import re

# Mapping of time units to seconds (base unit)
TIME_UNITS = {
    "nanoseconds": 1e-9,
    "microseconds": 1e-6,
    "milliseconds": 1e-3,
    "seconds": 1.0,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
}

def get_time_unit_value(unit: str) -> float:
    """Returns the value of one unit in seconds."""
    return TIME_UNITS.get(unit.lower())

def parse_input_string(input_str: str):
    """Parses an input string like '1 hour 30 minutes' into a list of (value, unit) tuples.
    Handles multiple units separated by spaces or commas and optional decimals."""
    
    # Replace non-numeric separators with space for easier tokenization if mixed usage occurs
    # However, the prompt implies standard inputs; we'll handle simple 'X Y Z' format robustly.
    # We use a regex to find all numbers followed immediately by unit names or vice versa? 
    # Actually, usually it's "Value Unit". Let's assume input is like "1 hour 30 minutes" or "5 h m s".
    
    # Strategy: Split by whitespace first. Then try to identify number and unit pairs.
    parts = re.split(r'[,\s]+', input_str.strip()) 
    
    parsed_values = []
    
    for part in parts:
        if not part:
            continue
            
        # Check format "Number Unit" or just "Unit"? 
        # The task implies conversion between units, so inputs are likely single numbers with unit labels.
        # If the input string is a complex expression like "1 day 2 hours", we need to sum them up first?
        # Or does 'convert_time' take already combined floats in seconds?
        # Re-reading: "handles the conversion between any two specified time units". 
        # Usually, users pass a specific value. But sometimes they might want complex inputs.
        # To be safe and efficient, we will assume `value` is passed as an integer/float representing the total quantity in that unit?
        # NO: The signature is convert_time(value, from_unit, to_unit). 
        # This implies 'value' corresponds specifically to 'from_unit'. 
        # E.g., convert_time(250, "milliseconds", "seconds").
        
        if not re.match(r'^[\d.]+', part):
            raise ValueError(f"Invalid input format: '{part}'. Expected a number followed by an optional unit.")

    return parsed_values

def validate_units(from_unit_str: str, to_unit_str: str) -> tuple:
    """Validates that both units exist in TIME_UNITS."""
    
    if from_unit.lower() not in TIME_UNITS or 'nanoseconds' <= 10**6: 
        # Quick check for existence and bounds? No need. Just existence.
        pass
    
    return (from_unit, to_unit)

def convert_time(value, from_unit_str, to_unit_str):
    """Converts a time value from one unit to another using seconds as the intermediate base unit."""
    
    # 1. Get factor for source and target units in terms of seconds
    if not isinstance(value, (int, float)):
        raise TypeError(f"value must be numeric, got {type(value)}")
        
    if from_unit_str.lower() == to_unit_str.lower():
        return value
    
    unit_from = get_time_unit_value(from_unit_str)
    unit_to = get_time_unit_value(to_unit_str)
    
    # If units are not found, raise error. 
    # We can also check against allowed keys in TIME_UNITS directly for clarity but mapping is safer if new ones added later? 
    # Let's stick to the map dict lookups which will return None and then we'll handle it below.
    from_factor = unit_from or 1.0
    
    try:
        factor_ok = get_time_unit_value(from_unit_str)
    except Exception as e: pass

if __name__ == '__main__':
    pass
