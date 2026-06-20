def convert_time(value, from_unit, to_unit):
    unit_to_seconds = {
        "millisecond": 0.001,
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2592000,
        "year": 31536000
    }
    
    if from_unit not in unit_to_seconds:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in unit_to_seconds:
        raise ValueError(f"Unknown unit: {to_unit}")
    
    value_in_seconds = value * unit_to_seconds[from_unit]
    converted_value = value_in_seconds / unit_to_seconds[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_time(3600, "second", "hour")
    print(result)