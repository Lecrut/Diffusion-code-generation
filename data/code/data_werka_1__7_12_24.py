def convert_time(value, from_unit, to_unit):
    conversion_factors = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800, 'months': 2592000, 'years': 31536000}
    value_in_seconds = value * conversion_factors[from_unit]
    converted_value = value_in_seconds / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    sample_value = 10
    from_unit = 'hours'
    to_unit = 'minutes'
    result = convert_time(sample_value, from_unit, to_unit)
    print(result)