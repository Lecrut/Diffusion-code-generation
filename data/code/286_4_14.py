conversion_factors = {
    'mm': 0.0393701,
}

def is_valid_unit(unit):
    return unit in conversion_factors

def convert_mm_to_in(mm):
    if not isinstance(mm, (int, float)):
        raise TypeError("Input must be a number")
    if not is_valid_unit('mm'):
        raise ValueError("Invalid unit")
    return mm * conversion_factors['mm']

if __name__ == '__main__':
    sample_value = 100
    print(convert_mm_to_in(sample_value))