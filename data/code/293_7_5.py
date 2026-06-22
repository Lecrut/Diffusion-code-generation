import math

def angle_conversion(value, from_unit, to_unit):
    if from_unit == 'degrees' and to_unit == 'radians':
        return value * (math.pi / 180)
    elif from_unit == 'degrees' and to_unit == 'gradians':
        return value * (200 / 180)
    elif from_unit == 'radians' and to_unit == 'degrees':
        return value * (180 / math.pi)
    elif from_unit == 'radians' and to_unit == 'gradians':
        return value * (200 / math.pi)
    elif from_unit == 'gradians' and to_unit == 'degrees':
        return value * (180 / 200)
    elif from_unit == 'gradians' and to_unit == 'radians':
        return value * (math.pi / 200)
    else:
        raise ValueError('Invalid unit conversion')
if __name__ == '__main__':
    print(angle_conversion(90, 'degrees', 'radians'))
    print(angle_conversion(90, 'degrees', 'gradians'))
    print(angle_conversion(math.pi, 'radians', 'degrees'))
    print(angle_conversion(math.pi, 'radians', 'gradians'))
    print(angle_conversion(200, 'gradians', 'degrees'))
    print(angle_conversion(200, 'gradians', 'radians'))