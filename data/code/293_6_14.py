SPEED_CONVERSION_KMH_TO_MPH = 0.621371
SPEED_CONVERSION_KMH_TO_MS = 1 / 3.6
SPEED_CONVERSION_MPH_TO_KMH = 1 / SPEED_CONVERSION_KMH_TO_MPH
SPEED_CONVERSION_MPH_TO_MS = 0.44704
SPEED_CONVERSION_MS_TO_KMH = 3.6
SPEED_CONVERSION_MS_TO_MPH = 1 / SPEED_CONVERSION_MPH_TO_MS

def convert_speed(value, from_unit, to_unit):
    if from_unit == 'km/h':
        if to_unit == 'mph':
            return value * SPEED_CONVERSION_KMH_TO_MPH
        elif to_unit == 'm/s':
            return value * SPEED_CONVERSION_KMH_TO_MS
        else:
            raise ValueError('Invalid units')
    elif from_unit == 'mph':
        if to_unit == 'km/h':
            return value * SPEED_CONVERSION_MPH_TO_KMH
        elif to_unit == 'm/s':
            return value * SPEED_CONVERSION_MPH_TO_MS
        else:
            raise ValueError('Invalid units')
    elif from_unit == 'm/s':
        if to_unit == 'km/h':
            return value * SPEED_CONVERSION_MS_TO_KMH
        elif to_unit == 'mph':
            return value * SPEED_CONVERSION_MS_TO_MPH
        else:
            raise ValueError('Invalid units')
    else:
        raise ValueError('Invalid units')
if __name__ == '__main__':
    print(convert_speed(100, 'km/h', 'mph'))
    print(convert_speed(100, 'km/h', 'm/s'))