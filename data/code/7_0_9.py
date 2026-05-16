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
        if target_unit == 'minutes':
            return time_value * 60.0
        elif target_unit == 'seconds':
            return time_value * 3600.0
    raise ValueError("Invalid source or target unit specified")
if __name__ == '__main__':
    time = 7200
    source = 'seconds'
    target = 'hours'
    result = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result} {target}")
    time = 180
    source = 'minutes'
    target = 'seconds'
    result = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result} {target}")
    time = 120
    source = 'hours'
    target = 'minutes'
    result = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result} {target}")
    time = 3600
    source = 'hours'
    target = 'seconds'
    result = convert_time(time, source, target)
    print(f"Converting {time} {source} to {target}: {result} {target}")