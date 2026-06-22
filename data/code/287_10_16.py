KG_TO_LB = 2.2046226218
LB_TO_KG = 1 / KG_TO_LB

def convert_weight(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Input value must be a number.')
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError('Units must be provided as strings.')
    if from_unit == to_unit:
        return value
    if from_unit == 'kg':
        if to_unit == 'lb':
            return value * KG_TO_LB
        elif to_unit == 'g':
            return value * 1000.0
        else:
            raise ValueError(f'Unsupported target unit: {to_unit}')
    elif from_unit == 'lb':
        if to_unit == 'kg':
            return value * LB_TO_KG
        elif to_unit == 'g':
            return value * 453.592
        else:
            raise ValueError(f'Unsupported target unit: {to_unit}')
if __name__ == '__main__':
    print(convert_weight(1, 'kg', 'lb'))
    print(convert_weight(1, 'lb', 'kg'))
    print(convert_weight(1000, 'g', 'kg'))