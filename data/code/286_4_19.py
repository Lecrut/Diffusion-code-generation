conversion_factors = {
    'mm': 1 / 25.4
}

def validate_unit(unit):
    if unit not in conversion_factors:
        raise ValueError(f"Invalid unit: {unit}")

def millimeters_to_inches(mm):
    validate_unit('mm')
    return mm * conversion_factors['mm']

if __name__ == '__main__':
    sample_mm = 100
    result = millimeters_to_inches(sample_mm)
    print(result)