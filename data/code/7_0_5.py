def convert_time(value, source_unit, target_unit):
    units = {'second': 1, 'minute': 60, 'hour': 3600}
    if source_unit not in units or target_unit not in units:
        raise ValueError("Invalid time unit. Use 'second', 'minute', or 'hour'.")
    seconds = value * units[source_unit]
    result = seconds / units[target_unit]
    return result

if __name__ == '__main__':
    print(convert_time(120, 'minute', 'hour'))
    print(convert_time(3.5, 'hour', 'minute'))
    print(convert_time(60, 'second', 'minute'))
    print(convert_time(0.5, 'hour', 'second'))