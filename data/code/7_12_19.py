def convert_time(value, from_unit, to_unit):
    conversion_to_seconds = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 1e-3,
        's': 1,
        'min': 60,
        'h': 3600,
        'd': 86400,
        'w': 604800
    }

    if from_unit not in conversion_to_seconds:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in conversion_to_seconds:
        raise ValueError(f"Unknown to_unit: {to_unit}")

    seconds = value * conversion_to_seconds[from_unit]
    result = seconds / conversion_to_seconds[to_unit]
    return result

if __name__ == '__main__':
    val = convert_time(1, 'h', 'min')
    print(val)
    
    val2 = convert_time(1000, 'ms', 's')
    print(val2)