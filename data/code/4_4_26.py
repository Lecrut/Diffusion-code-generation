def convert_distance(distance, target_unit):
    conversion_factors = {'meters_to_kilometers': 0.001, 'kilometers_to_meters': 1000, 'meters_to_feet': 3.28084, 'feet_to_meters': 0.3048, 'meters_to_inches': 39.3701, 'inches_to_meters': 0.0254}
    if distance == 0:
        return 0
    if target_unit == 'kilometers':
        conversion_key = 'meters_to_kilometers'
    elif target_unit == 'feet':
        conversion_key = 'meters_to_feet'
    elif target_unit == 'inches':
        conversion_key = 'meters_to_inches'
    else:
        raise ValueError('Unsupported target unit')
    converted_distance = distance * conversion_factors[conversion_key]
    return converted_distance
if __name__ == '__main__':
    sample_distance = 100
    target_unit = 'kilometers'
    result = convert_distance(sample_distance, target_unit)
    print(result)