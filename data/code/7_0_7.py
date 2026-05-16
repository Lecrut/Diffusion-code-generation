import math
def convert_time(time_value, source_unit, target_unit):
    if source_unit == target_unit:
        return time_value
    if source_unit == 'seconds':
        if target_unit == 'minutes':
            return time_value / 60.0
        elif target_unit == 'hours':
            return time_value / 3600.0
    elif source_unit == 'minutes':
        if target_unit == 'seconds':
            return time_value * 60.0
        elif target_unit == 'hours':
            return time_value / 60.0
    elif source_unit == 'hours':
        if target_unit == 'seconds':
            return time_value * 3600.0
        elif target_unit == 'minutes':
            return time_value * 60.0
    raise ValueError("Invalid source or target unit specified")
if __name__ == '__main__':
    time = 3665
    source = 'seconds'
    target = 'minutes'
    result1 = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result1}")
    time = 180
    source = 'minutes'
    target = 'hours'
    result2 = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result2}")
    time = 7200
    source = 'hours'
    target = 'seconds'
    result3 = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result3}")
    time = 3600
    source = 'hours'
    target = 'minutes'
    result4 = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result4}")