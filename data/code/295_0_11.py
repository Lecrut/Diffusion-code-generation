CONVERSION_FACTOR = 1e-3

def meters_to_kilometers(meters):
    return float(f"{meters * CONVERSION_FACTOR:.2f}")

if __name__ == '__main__':
    meters_value = 1000.0
    kilometers_value = meters_to_kilometers(meters_value)
    print(f"{meters_value} meters is equal to {kilometers_value} kilometers")