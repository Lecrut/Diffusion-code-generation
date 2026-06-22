def convert_time(value, source_unit, target_unit):
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    valid_units = ("seconds", "minutes", "hours")
    if source_unit not in valid_units:
        raise ValueError(f"Invalid source_unit: {source_unit}. Must be one of {valid_units}")
    if target_unit not in valid_units:
        raise ValueError(f"Invalid target_unit: {target_unit}. Must be one of {valid_units}")
    
    if source_unit == target_unit:
        return value
    
    if source_unit == "seconds":
        if target_unit == "minutes":
            return value / 60
        elif target_unit == "hours":
            return value / 3600
    elif source_unit == "minutes":
        if target_unit == "seconds":
            return value * 60
        elif target_unit == "hours":
            return value / 60
    elif source_unit == "hours":
        if target_unit == "seconds":
            return value * 3600
        elif target_unit == "minutes":
            return value * 60

if __name__ == '__main__':
    result = convert_time(3600, "seconds", "hours")
    print(result)
    
    result2 = convert_time(2.5, "hours", "minutes")
    print(result2)
    
    result3 = convert_time(120, "minutes", "seconds")
    print(result3)