def convert_time(value, source_unit, target_unit):
    units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    if source_unit not in units or target_unit not in units:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

    seconds = value * units[source_unit]
    result = seconds / units[target_unit]

    return result

if __name__ == '__main__':
    sample_value = 90
    sample_source = 'minutes'
    sample_target = 'seconds'
    result = convert_time(sample_value, sample_source, sample_target)
    print(result)

    sample_value2 = 3.5
    sample_source2 = 'hours'
    sample_target2 = 'minutes'
    result2 = convert_time(sample_value2, sample_source2, sample_target2)
    print(result2)

    sample_value3 = 7200
    sample_source3 = 'seconds'
    sample_target3 = 'hours'
    result3 = convert_time(sample_value3, sample_source3, sample_target3)
    print(result3)