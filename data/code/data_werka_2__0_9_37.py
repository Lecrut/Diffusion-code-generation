CONVERSION_FACTORS = {
    'meters_to_feet': 3.28084,
}

def convert_length(value, conversion_type):
    if conversion_type not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion type: {conversion_type}")
    return value * CONVERSION_FACTORS[conversion_type]

if __name__ == '__main__':
    sample_value = 10
    result = convert_length(sample_value, 'meters_to_feet')
    print(result)