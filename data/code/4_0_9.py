def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    valid_units = {'m', 'meter', 'meters', 'km', 'kilometer', 'kilometers', 'mi', 'mile', 'miles'}
    
    if from_unit not in valid_units:
        raise ValueError(f"Invalid from_unit: {from_unit}. Must be one of {valid_units}")
    if to_unit not in valid_units:
        raise ValueError(f"Invalid to_unit: {to_unit}. Must be one of {valid_units}")
    
    def to_meters(val, unit):
        if unit in ('m', 'meter', 'meters'):
            return val
        elif unit in ('km', 'kilometer', 'kilometers'):
            return val * 1000
        elif unit in ('mi', 'mile', 'miles'):
            return val * 1609.344
    
    def from_meters(val, unit):
        if unit in ('m', 'meter', 'meters'):
            return val
        elif unit in ('km', 'kilometer', 'kilometers'):
            return val / 1000
        elif unit in ('mi', 'mile', 'miles'):
            return val / 1609.344
    
    meters = to_meters(value, from_unit)
    result = from_meters(meters, to_unit)
    
    return result

if __name__ == '__main__':
    print(convert_distance(1000, 'm', 'km'))
    print(convert_distance(5, 'km', 'm'))
    print(convert_distance(1, 'mi', 'km'))
    print(convert_distance(10, 'miles', 'meters'))
    print(convert_distance(1609.344, 'm', 'mi'))