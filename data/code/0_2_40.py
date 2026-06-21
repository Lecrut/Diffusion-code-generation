CONVERSION_FACTORS = {
    'inches_to_centimeters': 2.54
}

def convert_length(length, unit):
    if unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported unit: {unit}")
    return length * CONVERSION_FACTORS[unit]

if __name__ == '__main__':
    print(convert_length(1, 'inches_to_centimeters'))
    print(convert_length(10, 'inches_to_centimeters'))
    print(convert_length(0.5, 'inches_to_centimeters'))