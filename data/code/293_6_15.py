def convert_speed(value, from_unit, to_unit):
    if from_unit == 'km/h' and to_unit == 'mph':
        return value * 0.621371
    elif from_unit == 'mph' and to_unit == 'km/h':
        return value / 0.621371
    elif from_unit == 'km/h' and to_unit == 'm/s':
        return value / 3.6
    elif from_unit == 'm/s' and to_unit == 'km/h':
        return value * 3.6
    elif from_unit == 'mph' and to_unit == 'm/s':
        return value * 0.44704
    elif from_unit == 'm/s' and to_unit == 'mph':
        return value / 0.44704
    else:
        raise ValueError('Invalid units')
if __name__ == '__main__':
    print(convert_speed(100, 'km/h', 'mph'))
    print(convert_speed(50, 'mph', 'km/h'))
    print(convert_speed(30, 'km/h', 'm/s'))
    print(convert_speed(10, 'm/s', 'km/h'))
    print(convert_speed(60, 'mph', 'm/s'))
    print(convert_speed(5, 'm/s', 'mph'))