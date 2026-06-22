def convert_distance(distance, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'mi': 1609.34, 'ft': 0.3048, 'yd': 0.9144, 'in': 0.0254}
    distance_in_meters = distance * conversion_factors[unit]
    converted_distances = {unit: distance / conversion_factors[unit] for unit in conversion_factors}
    return converted_distances
if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    result = convert_distance(sample_distance, sample_unit)
    print(result)