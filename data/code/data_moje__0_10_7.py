def convert_length(length, target_unit):
    conversions = {
        'meters': lambda x: x,
        'feet': lambda x: x * 3.28084,
        'kilometers': lambda x: x / 1000.0
    }
    
    if target_unit not in conversions:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return conversions[target_unit](length)

if __name__ == '__main__':
    sample_value = 100.0
    sample_units = ['meters', 'feet', 'kilometers']
    
    for unit in sample_units:
        result = convert_length(sample_value, unit)
        print(f"{sample_value} meters to {unit}: {result}")
    
    try:
        convert_length(10, 'inches')
    except ValueError as e:
        print(f"Error caught: {e}")