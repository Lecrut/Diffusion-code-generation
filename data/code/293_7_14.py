import math
DEGREES_TO_RADIANS = math.pi / 180
RADIANS_TO_DEGREES = 180 / math.pi
GRADIENTS_TO_RADIANS = math.pi / 200
RADIANS_TO_GRADIENTS = 200 / math.pi

def convert_angle(value, from_unit, to_unit):
    if from_unit == 'degrees':
        value_in_radians = value * DEGREES_TO_RADIANS
    elif from_unit == 'radians':
        value_in_radians = value
    elif from_unit == 'gradians':
        value_in_radians = value * GRADIENTS_TO_RADIANS
    else:
        raise ValueError('Invalid input unit')
    if to_unit == 'degrees':
        result = value_in_radians * RADIANS_TO_DEGREES
    elif to_unit == 'radians':
        result = value_in_radians
    elif to_unit == 'gradians':
        result = value_in_radians * RADIANS_TO_GRADIENTS
    else:
        raise ValueError('Invalid output unit')
    return result
if __name__ == '__main__':
    print(convert_angle(90, 'degrees', 'radians'))
    print(convert_angle(math.pi, 'radians', 'gradians'))
    print(convert_angle(400, 'gradians', 'degrees'))