CONVERSION_RATE = {
    'liters_to_gallons': 0.264172
}

def convert_volume(volume, conversion_key):
    if conversion_key not in CONVERSION_RATE:
        raise ValueError("Unsupported conversion type")
    return volume * CONVERSION_RATE[conversion_key]

if __name__ == '__main__':
    sample_values = [1.5, 3.0, 4.5, 6.0]
    for value in sample_values:
        print(f"{value} liters is {convert_volume(value, 'liters_to_gallons')} gallons")