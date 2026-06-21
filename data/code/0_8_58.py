def convert_length(length, target_unit):
    METER_TO_FEET = 3.28084
    METER_TO_KILOMETERS = 0.001

    supported_units = {
        'meters': length,
        'feet': length * METER_TO_FEET,
        'kilometers': length * METER_TO_KILOMETERS
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return supported_units[target_unit]

if __name__ == '__main__':
    sample_length = 150
    sample_unit = 'kilometers'
    converted_value = convert_length(sample_length, sample_unit)
    print(converted_value)