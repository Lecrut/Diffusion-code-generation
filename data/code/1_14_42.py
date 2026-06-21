CONVERSION_RATE = {
    'kg_to_pounds': 2.20462,
    'pounds_to_kg': 1 / 2.20462
}

def convert_weight(value, conversion_type):
    if conversion_type not in CONVERSION_RATE:
        raise ValueError("Unsupported conversion type")
    return value * CONVERSION_RATE[conversion_type]

if __name__ == '__main__':
    sample_kg = 70
    sample_pounds = 154.32
    converted_pounds = convert_weight(sample_kg, 'kg_to_pounds')
    converted_kg = convert_weight(sample_pounds, 'pounds_to_kg')
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")