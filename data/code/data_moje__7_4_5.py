def convert_time(value, from_unit, to_unit):
    seconds_per_year = 365.25 * 24 * 60 * 60
    seconds_per_month = 30.44 * 24 * 60 * 60
    seconds_per_day = 24 * 60 * 60
    seconds_per_hour = 60 * 60
    seconds_per_minute = 60
    seconds_per_second = 1

    unit_to_seconds = {
        'years': seconds_per_year,
        'months': seconds_per_month,
        'days': seconds_per_day,
        'hours': seconds_per_hour,
        'minutes': seconds_per_minute,
        'seconds': seconds_per_second
    }

    if from_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

    total_seconds = value * unit_to_seconds[from_unit]
    converted_value = total_seconds / unit_to_seconds[to_unit]
    
    return converted_value

if __name__ == '__main__':
    years_value = 2.5
    days_value = convert_time(years_value, 'years', 'days')
    print(days_value)
    
    hours_value = convert_time(days_value, 'days', 'hours')
    print(hours_value)
    
    minutes_value = convert_time(hours_value, 'hours', 'minutes')
    print(minutes_value)
    
    seconds_value = convert_time(minutes_value, 'minutes', 'seconds')
    print(seconds_value)