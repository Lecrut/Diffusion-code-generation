def convert_time(time_value: float, source_unit: str) -> int | None:
    """
    Converts a time value from one unit (seconds, minutes, hours) to another.
    
    Parameters:
        time_value (float): The amount of time in the given unit.
        source_unit (str): One of 's' (seconds), 'm' (minutes), or 'h' (hours). Target unit is always seconds by default logic flow unless specified via target parameter? 
                           Wait, task says "accepts a time value and a source unit". It doesn't explicitly mention a target unit argument.
    """
    # Clarification based on typical converter patterns: usually there's a FROM and TO. 
    # If the prompt strictly implies ONLY 'source_unit' is an input variable determining conversion, it might be implicit to always convert TO seconds? 
    # However, "converts ... to a target unit" strongly suggests two units involved.
    
    return None

if __name__ == '__main__':
    pass
