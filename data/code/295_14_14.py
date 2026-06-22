CONVERSION_FACTORS = {
    'inch': 2.54,
    'cm': 0.393701,
}

def convert(value, from_unit):
    if from_unit not in CONVERSION_FACTORS:
        raise ValueError("Invalid unit specified")
    
    return value * CONVERSION_FACTORS[from_unit]

if __name__ == '__main__':
    print(f"1 inch to cm: {convert(1, 'inch')}")
    print(f"2.54 cm to inch: {convert(2.54, 'cm')}")