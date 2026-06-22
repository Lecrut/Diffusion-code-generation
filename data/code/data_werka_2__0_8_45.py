METERS_TO_FEET = 3.28084
METERS_TO_KILOMETERS = 0.001

def convert_length(length, target_unit):
    supported_units = {
        'meters': length,
        'feet': length * METERS_TO_FEET,
        'kilometers': length * METERS_TO_KILOMETERS
    }
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return supported_units[target_unit]

if __name__ == '__main__':
    sample_length = 150
    target_unit = 'meters'
    converted_value = convert_length(sample_length, target_unit)
    print(converted_value)