conversion_factors = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800}

def convert_time(value, from_unit, to_unit):
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]
if __name__ == '__main__':
    print(convert_time(1, 'hours', 'minutes'))
    print(convert_time(24, 'hours', 'days'))
    print(convert_time(7, 'weeks', 'days'))