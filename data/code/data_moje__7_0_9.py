def convert_time(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value

    seconds_map = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600
    }

    if source_unit not in seconds_map or target_unit not in seconds_map:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

    value_in_seconds = value * seconds_map[source_unit]
    converted_value = value_in_seconds / seconds_map[target_unit]

    if converted_value == int(converted_value):
        return int(converted_value)
    
    return converted_value

if __name__ == '__main__':
    result = convert_time(2, "hours", "minutes")
    print(result)