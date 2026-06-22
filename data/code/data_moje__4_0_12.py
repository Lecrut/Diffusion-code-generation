def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative.")
    
    meters = 0.0
    
    if from_unit == 'meters':
        meters = value
    elif from_unit == 'kilometers':
        meters = value * 1000.0
    elif from_unit == 'miles':
        meters = value * 1609.344
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")
    
    if to_unit == 'meters':
        return meters
    elif to_unit == 'kilometers':
        return meters / 1000.0
    elif to_unit == 'miles':
        return meters / 1609.344
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")

if __name__ == '__main__':
    print(convert_distance(5.0, 'kilometers', 'miles'))
    print(convert_distance(1.0, 'miles', 'kilometers'))
    print(convert_distance(1000.0, 'meters', 'kilometers'))