def convert_time(value, from_unit, to_unit):
    conversion_factors = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800, 'months': 2629743, 'years': 31556926}
    value_in_seconds = value * conversion_factors[from_unit]
    converted_value = value_in_seconds / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    value = 10
    from_unit = 'hours'
    to_unit = 'minutes'
    result = convert_time(value, from_unit, to_unit)
    print(result)