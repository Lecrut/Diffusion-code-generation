def convert_length(value, conversion_table):
    try:
        return value * conversion_table['cm_to_in']
    except KeyError as e:
        raise ValueError(f"Unsupported conversion key: {e}")

if __name__ == '__main__':
    sample_cm = 50
    conversion_factors = {
        'cm_to_in': 1 / 2.54
    }
    inches = convert_length(sample_cm, conversion_factors)
    print(inches)