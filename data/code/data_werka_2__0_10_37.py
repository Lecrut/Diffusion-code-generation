CONVERSION_FACTORS = {
    'cm_to_in': 1 / 2.54
}

def convert_length(value, conversion_key):
    if conversion_key not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion key: {conversion_key}")
    return value * CONVERSION_FACTORS[conversion_key]

if __name__ == '__main__':
    sample_cm = 50
    inches = convert_length(sample_cm, 'cm_to_in')
    print(inches)