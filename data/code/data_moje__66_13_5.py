CONVERSION_FACTOR = 1000
convert_km_to_m = lambda value: value * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 5
    print(convert_km_to_m(sample_value))