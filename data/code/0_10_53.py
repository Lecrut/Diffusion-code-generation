CONVERSION_TABLE = {
    'cm': {'inches': 1 / 2.54}
}

def convert_unit(value, from_unit, to_unit):
    if from_unit not in CONVERSION_TABLE or to_unit not in CONVERSION_TABLE[from_unit]:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    factor = CONVERSION_TABLE[from_unit][to_unit]
    return value * factor

if __name__ == '__main__':
    sample_cm = 50
    inches = convert_unit(sample_cm, 'cm', 'inches')
    print(inches)