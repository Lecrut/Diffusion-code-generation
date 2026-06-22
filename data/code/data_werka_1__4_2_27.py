def convert_distance(distance, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}
    meters = distance * conversion_factors[unit]
    converted_distances = {unit: meters / conversion_factors[unit] for unit in conversion_factors}
    return converted_distances
if __name__ == '__main__':
    sample_distance = 5.0
    sample_unit = 'km'
    result = convert_distance(sample_distance, sample_unit)
    print(result)