import math

def convert_angle(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in ('degrees', 'radians', 'gradians'):
        raise ValueError("From unit must be 'degrees', 'radians', or 'gradians'.")
    
    if to_unit not in ('degrees', 'radians', 'gradians'):
        raise ValueError("To unit must be 'degrees', 'radians', or 'gradians'.")
    
    if from_unit == 'degrees':
        value = math.radians(value)
    elif from_unit == 'gradians':
        value = math.radians(value * (math.pi / 200))
    
    if to_unit == 'gradians':
        return value * (200 / math.pi)
    elif to_unit == 'radians':
        return value
    
    return math.degrees(value)

if __name__ == '__main__':
    print(convert_angle(90, 'degrees', 'radians'))
    print(convert_angle(math.pi, 'radians', 'gradians'))
    print(convert_angle(400, 'gradians', 'degrees'))