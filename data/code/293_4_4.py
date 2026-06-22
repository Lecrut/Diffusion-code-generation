def time_converter(value, from_unit, to_unit):
    conversion_factors = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Invalid unit')
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])
if __name__ == '__main__':
    print(time_converter(1, 'hours', 'minutes'))
    print(time_converter(24, 'days', 'seconds'))
    print(time_converter(7, 'weeks', 'hours'))