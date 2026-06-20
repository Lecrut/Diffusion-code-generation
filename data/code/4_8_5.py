def convert_distance(value, unit):
    if unit == 'km':
        miles = value * 0.621371
        return {'original_value': value, 'original_unit': unit, 'converted_value': miles, 'converted_unit': 'miles'}
    if unit == 'miles':
        kilometers = value / 0.621371
        return {'original_value': value, 'original_unit': unit, 'converted_value': kilometers, 'converted_unit': 'kilometers'}
    raise ValueError("Unit must be 'km' or 'miles'")

if __name__ == '__main__':
    result1 = convert_distance(10, 'km')
    print(f"{result1['original_value']} {result1['original_unit']} is {result1['converted_value']} {result1['converted_unit']}")
    
    result2 = convert_distance(5, 'miles')
    print(f"{result2['original_value']} {result2['original_unit']} is {result2['converted_value']} {result2['converted_unit']}")