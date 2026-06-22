def time_converter(value, from_unit, to_unit):
    conversion_factors = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Invalid unit')
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])
if __name__ == '__main__':
    print(time_converter(1, 'h', 'm'))
    print(time_converter(24, 'd', 's'))
    print(time_converter(7, 'w', 'h'))