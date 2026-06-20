def convert_distance(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344
    }
    
    if from_unit.lower() not in units or to_unit.lower() not in units:
        raise ValueError("Invalid unit. Supported units: meters, kilometers, miles")
    
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    meters = value * units[from_unit.lower()]
    return meters / units[to_unit.lower()]

if __name__ == '__main__':
    sample_value = 5
    sample_from = 'kilometers'
    sample_to = 'miles'
    result = convert_distance(sample_value, sample_from, sample_to)
    print(f"{sample_value} {sample_from} is {result} {sample_to}")
    
    sample_value_2 = 100
    sample_from_2 = 'miles'
    sample_to_2 = 'meters'
    result_2 = convert_distance(sample_value_2, sample_from_2, sample_to_2)
    print(f"{sample_value_2} {sample_from_2} is {result_2} {sample_to_2}")
    
    try:
        convert_distance(-10, 'meters', 'kilometers')
    except ValueError as e:
        print(f"Error caught: {e}")