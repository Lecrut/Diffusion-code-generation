CONVERSION_TABLE = {
    'cubic_centimeters_to_cubic_inches': 0.0610237440947
}

def convert_volume(volume, from_unit, to_unit):
    key = f'{from_unit}_to_{to_unit}'
    if key not in CONVERSION_TABLE:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
    conversion_factor = CONVERSION_TABLE[key]
    return volume * conversion_factor

if __name__ == '__main__':
    sample_values = [100, 500, 1000]
    for value in sample_values:
        result = convert_volume(value, 'cubic_centimeters', 'cubic_inches')
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')