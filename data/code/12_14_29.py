KILOGRAMS_TO_POUNDS = 2.20462262185
POUNDS_TO_KILOGRAMS = 1 / KILOGRAMS_TO_POUNDS

def convert_weight(weight, to_unit):
    if to_unit == 'kg':
        return weight * POUNDS_TO_KILOGRAMS
    elif to_unit == 'lb':
        return weight * KILOGRAMS_TO_POUNDS
    else:
        raise ValueError("to_unit must be 'kg' or 'lb'")
if __name__ == '__main__':
    sample_weight_kg = 75.0
    sample_weight_lb = 165.3467
    converted_to_pounds = convert_weight(sample_weight_kg, 'lb')
    converted_to_kilograms = convert_weight(sample_weight_lb, 'kg')
    print(f'{sample_weight_kg} kg is {converted_to_pounds:.2f} lb')
    print(f'{sample_weight_lb} lb is {converted_to_kilograms:.2f} kg')