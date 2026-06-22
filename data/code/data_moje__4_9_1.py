def convert_distance(value, unit, target_unit):
    if unit == target_unit:
        return value
    
    miles_to_km = 1.60934
    
    if unit == 'miles' and target_unit == 'kilometers':
        return value * miles_to_km
    elif unit == 'kilometers' and target_unit == 'miles':
        return value / miles_to_km
    else:
        raise ValueError(f"Unsupported unit conversion: {unit} to {target_unit}")

if __name__ == '__main__':
    result = convert_distance(5.0, 'miles', 'kilometers')
    print(result)
    
    result2 = convert_distance(10.0, 'kilometers', 'miles')
    print(result2)