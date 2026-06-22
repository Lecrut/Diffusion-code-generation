import math

def angle_conversion(value, from_unit, to_unit):
    if from_unit == 'degrees':
        value_in_radians = math.radians(value)
    elif from_unit == 'radians':
        value_in_radians = value
    elif from_unit == 'gradians':
        value_in_radians = math.radians(value * (math.pi / 200))
    else:
        raise ValueError("Invalid input unit. Choose from 'degrees', 'radians', or 'gradians'.")
    if to_unit == 'degrees':
        return math.degrees(value_in_radians)
    elif to_unit == 'radians':
        return value_in_radians
    elif to_unit == 'gradians':
        return value_in_radians * (200 / math.pi)
    else:
        raise ValueError("Invalid output unit. Choose from 'degrees', 'radians', or 'gradians'.")
if __name__ == '__main__':
    print(angle_conversion(45, 'degrees', 'radians'))
    print(angle_conversion(math.pi / 2, 'radians', 'gradians'))
    print(angle_conversion(200, 'gradians', 'degrees'))