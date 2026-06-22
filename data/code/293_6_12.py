def convert_speed(value, from_unit, to_unit):
    conversion_factors = {'km/h': {'m/s': 0.27778, 'mph': 0.62137}, 'mph': {'m/s': 0.44704, 'km/h': 1.60934}, 'm/s': {'km/h': 3.6, 'mph': 2.23694}}
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    print(convert_speed(100, 'km/h', 'mph'))
    print(convert_speed(50, 'm/s', 'km/h'))
    print(convert_speed(30, 'mph', 'm/s'))