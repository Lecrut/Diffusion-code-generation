CONVERSION_FACTORS = {
    'km_to_m': 1000.0,
    'm_to_km': 0.001
}

def km_to_m(kilometers):
    factor = CONVERSION_FACTORS['km_to_m']
    return float(kilometers) * factor

if __name__ == '__main__':
    test_values = [1.0, 0.5, 123.456, 0.0001]
    for val in test_values:
        meters = km_to_m(val)
        print(meters)