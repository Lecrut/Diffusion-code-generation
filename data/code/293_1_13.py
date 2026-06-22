def convert_distance(value, from_unit, to_unit):
    if from_unit == 'km' and to_unit == 'mi':
        return value * 0.621371
    elif from_unit == 'mi' and to_unit == 'km':
        return value / 0.621371
    else:
        raise ValueError('Invalid units for distance conversion')
if __name__ == '__main__':
    print(convert_distance(1, 'km', 'mi'))
    print(convert_distance(5, 'mi', 'km'))