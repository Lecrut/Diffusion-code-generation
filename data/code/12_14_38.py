CONVERSION_FACTORS = {
    'kg_to_pounds': 2.2046226218487757,
    'pounds_to_kg': 1 / 2.2046226218487757
}

def convert_weight(value, conversion_type):
    if conversion_type not in CONVERSION_FACTORS:
        raise ValueError("Unsupported conversion type")
    return value * CONVERSION_FACTORS[conversion_type]

if __name__ == '__main__':
    sample_kg = 70
    sample_pounds = 154
    converted_to_pounds = convert_weight(sample_kg, 'kg_to_pounds')
    converted_to_kg = convert_weight(sample_pounds, 'pounds_to_kg')
    print(f"{sample_kg} kg is {converted_to_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_to_kg:.2f} kg")