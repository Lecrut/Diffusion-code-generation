def convert_time(value, source_unit, target_unit):
    units = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600
    }
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if source_unit_lower not in units:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_unit_lower not in units:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    seconds = value * units[source_unit_lower]
    result = seconds / units[target_unit_lower]
    
    return result

if __name__ == "__main__":
    print(convert_time(120, "minutes", "seconds"))
    print(convert_time(7200, "seconds", "hours"))
    print(convert_time(1.5, "hours", "minutes"))