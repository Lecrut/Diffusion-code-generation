def convert_time(value, source_unit, target_unit):
    units = {'seconds': 1, 'minutes': 60, 'hours': 3600}
    if source_unit not in units or target_unit not in units:
        raise ValueError(f"Invalid unit: {source_unit if source_unit not in units else target_unit}")
    
    seconds = value * units[source_unit]
    return seconds / units[target_unit]

if __name__ == '__main__':
    result1 = convert_time(60, 'seconds', 'minutes')
    result2 = convert_time(2, 'hours', 'minutes')
    result3 = convert_time(90, 'minutes', 'hours')
    print(result1)
    print(result2)
    print(result3)