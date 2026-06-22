CONVERSION_TABLE = {
    'pints_to_quarts': 0.5
}

def convert_volume(volume, conversion_key):
    if conversion_key not in CONVERSION_TABLE:
        raise ValueError(f"Unsupported conversion key: {conversion_key}")
    return volume * CONVERSION_TABLE[conversion_key]

if __name__ == '__main__':
    sample_pints = 12
    quarts = convert_volume(sample_pints, 'pints_to_quarts')
    print(quarts)