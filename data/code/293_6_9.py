CONVERSION_FACTOR_KMH_TO_MPH = 0.621371
CONVERSION_FACTOR_KMH_TO_MS = 1 / 3.6
CONVERSION_FACTOR_MPH_TO_KMH = 1 / CONVERSION_FACTOR_KMH_TO_MPH
CONVERSION_FACTOR_MPH_TO_MS = 0.44704
CONVERSION_FACTOR_MS_TO_KMH = 3.6
CONVERSION_FACTOR_MS_TO_MPH = 1 / CONVERSION_FACTOR_MPH_TO_MS

def convert_speed(value, from_unit, to_unit):
    if from_unit == 'km/h' and to_unit == 'mph':
        return value * CONVERSION_FACTOR_KMH_TO_MPH
    elif from_unit == 'km/h' and to_unit == 'm/s':
        return value * CONVERSION_FACTOR_KMH_TO_MS
    elif from_unit == 'mph' and to_unit == 'km/h':
        return value * CONVERSION_FACTOR_MPH_TO_KMH
    elif from_unit == 'mph' and to_unit == 'm/s':
        return value * CONVERSION_FACTOR_MPH_TO_MS
    elif from_unit == 'm/s' and to_unit == 'km/h':
        return value * CONVERSION_FACTOR_MS_TO_KMH
    elif from_unit == 'm/s' and to_unit == 'mph':
        return value * CONVERSION_FACTOR_MS_TO_MPH
    else:
        raise ValueError('Invalid units')
if __name__ == '__main__':
    print(convert_speed(100, 'km/h', 'mph'))
    print(convert_speed(100, 'km/h', 'm/s'))
    print(convert_speed(62.1371, 'mph', 'km/h'))
    print(convert_speed(62.1371, 'mph', 'm/s'))
    print(convert_speed(27.7778, 'm/s', 'km/h'))
    print(convert_speed(27.7778, 'm/s', 'mph'))