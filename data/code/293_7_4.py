import math

def angle_conversion(value, from_unit='degrees', to_unit='radians'):
    if from_unit == 'degrees':
        value = math.radians(value)
    elif from_unit == 'gradians':
        value = math.radians(value * (math.pi / 200))
    if to_unit == 'radians':
        return value
    elif to_unit == 'degrees':
        return math.degrees(value)
    elif to_unit == 'gradians':
        return value * (200 / math.pi)
if __name__ == '__main__':
    print(angle_conversion(180, 'degrees', 'radians'))
    print(angle_conversion(200, 'gradians', 'degrees'))