CENTS_MULTIPLIER = 100

def convert_to_cents(dollar_value):
    scaled = dollar_value * CENTS_MULTIPLIER
    rounded = round(scaled)
    return int(rounded)

if __name__ == '__main__':
    samples = [10.50, 0.01, 123.456, -5.25, 0.005, 100.0]
    for s in samples:
        print(convert_to_cents(s))