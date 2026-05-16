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
    time1 = 3600
    source1 = 'seconds'
    target1 = 'minutes'
    result1 = convert_time(time1, source1, target1)
    print(f"Convert {time1} {source1} to {target1}: {result1}")
    time2 = 120
    source2 = 'minutes'
    target2 = 'hours'
    result2 = convert_time(time2, source2, target2)
    print(f"Convert {time2} {source2} to {target2}: {result2}")
    time3 = 7200
    source3 = 'hours'
    target3 = 'seconds'
    result3 = convert_time(time3, source3, target3)
    print(f"Convert {time3} {source3} to {target3}: {result3}")
    time4 = 3600
    source4 = 'hours'
    target4 = 'minutes'
    result4 = convert_time(time4, source4, target4)
    print(f"Convert {time4} {source4} to {target4}: {result4}")