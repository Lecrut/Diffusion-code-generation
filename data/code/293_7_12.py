import math

def angle_conversion(value, from_unit, to_unit):
    if from_unit == 'degrees':
        value = math.radians(value)
    elif from_unit == 'gradians':
        value = math.radians(value * (math.pi / 200))
    if to_unit == 'degrees':
        return math.degrees(value)
    elif to_unit == 'gradians':
        return value * (200 / math.pi)
    return value
if __name__ == '__main__':
    print(angle_conversion(90, 'degrees', 'radians'))
    print(angle_conversion(math.pi, 'radians', 'gradians'))
    print(angle_conversion(400, 'gradians', 'degrees'))