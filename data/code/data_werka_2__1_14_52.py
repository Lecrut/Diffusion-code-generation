CONVERSION_TABLE = {
    'kg_to_pounds': 2.20462,
    'pounds_to_kg': 1 / 2.20462
}

def convert_weight(value, conversion_type):
    if conversion_type not in CONVERSION_TABLE:
        raise ValueError("Unsupported conversion type")
    return value * CONVERSION_TABLE[conversion_type]

if __name__ == '__main__':
    sample_weights = {
        'kg': 90,
        'pounds': 198.42
    }
    
    converted_pounds = convert_weight(sample_weights['kg'], 'kg_to_pounds')
    converted_kg = convert_weight(sample_weights['pounds'], 'pounds_to_kg')
    
    print(f"{sample_weights['kg']} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_weights['pounds']} pounds is {converted_kg:.2f} kg")