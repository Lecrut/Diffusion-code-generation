def time_converter(value, from_unit, to_unit):
    conversion_factors = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])
if __name__ == '__main__':
    print(time_converter(1, 'h', 'm'))
    print(time_converter(2, 'd', 's'))
    print(time_converter(3, 'w', 'h'))