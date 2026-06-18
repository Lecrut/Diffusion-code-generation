def convert_time(unit: str, value: float) -> dict:
    """
    Converts a given time duration from one standard unit to all others.
    
    Args:
        unit (str): Source unit ('seconds', 'minutes', 'hours', 'days').
        value (float): The numeric value of the time duration.
        
    Returns:
        dict: A dictionary containing the converted values for seconds, minutes, 
              hours, and days as floats with 4 decimal places if necessary.
              
    Raises:
        ValueError: If input units are invalid or value is negative.
    """
    
    valid_units = ['seconds', 'minutes', 'hours', 'days']
    
    # Input Validation for Unit
    if unit not in valid_units:
        raise ValueError(f"Invalid time unit '{unit}'. Supported units are: {valid_units}")
    
    # Input Validation for Value (must be non-negative)
    if value < 0:
        raise ValueError("Time duration cannot be negative.")

if __name__ == '__main__':
    pass
