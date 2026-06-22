import math

def convert_angle(value, from_unit='degrees', to_unit='radians'):
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
    print(convert_angle(90, 'degrees', 'radians'))
    print(convert_angle(math.pi, 'radians', 'gradians'))
    print(convert_angle(400, 'gradians', 'degrees'))