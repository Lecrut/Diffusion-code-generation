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
    return None
if __name__ == '__main__':
    time_s = 3600
    source = 'seconds'
    target = 'minutes'
    result1 = convert_time(time_s, source, target)
    print(f"Convert {time_s} {source} to {target}: {result1}")
    time_m = 120
    source = 'minutes'
    target = 'hours'
    result2 = convert_time(time_m, source, target)
    print(f"Convert {time_m} {source} to {target}: {result2}")
    time_h = 7200
    source = 'hours'
    target = 'seconds'
    result3 = convert_time(time_h, source, target)
    print(f"Convert {time_h} {source} to {target}: {result3}")
    time_s_to_s = 120
    source = 'seconds'
    target = 'seconds'
    result4 = convert_time(time_s_to_s, source, target)
    print(f"Convert {time_s_to_s} {source} to {target}: {result4}")