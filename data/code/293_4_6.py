def convert_time(value, from_unit, to_unit):
    conversion_factors = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])
if __name__ == '__main__':
    print(convert_time(1, 'h', 'm'))
    print(convert_time(7, 'd', 'w'))