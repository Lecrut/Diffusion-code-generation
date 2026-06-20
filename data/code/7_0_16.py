def convert_time(time_value, source_unit, target_unit):
    units_to_seconds = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600
    }
    
    if source_unit not in units_to_seconds or target_unit not in units_to_seconds:
        raise ValueError("Unsupported unit. Use 'seconds', 'minutes', or 'hours'.")
    
    if time_value < 0:
        raise ValueError("Time value must be non-negative.")
        
    seconds = time_value * units_to_seconds[source_unit]
    result = seconds / units_to_seconds[target_unit]
    return result

if __name__ == '__main__':
    result = convert_time(1.5, "hours", "seconds")
    print(result)