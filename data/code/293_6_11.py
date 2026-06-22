def convert_speed(value, from_unit, to_unit):
    conversions = {
        'km/h': {'mph': 0.621371, 'm/s': 1/3.6},
        'mph': {'km/h': 1/0.621371, 'm/s': 0.44704},
        'm/s': {'km/h': 3.6, 'mph': 1/0.44704}
    }
    
    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        raise ValueError('Invalid units')
    
    return value * conversions[from_unit][to_unit]

if __name__ == '__main__':
    print(convert_speed(100, 'km/h', 'mph'))
    print(convert_speed(62.1371, 'mph', 'km/h'))
    print(convert_speed(1/3.6, 'm/s', 'km/h'))