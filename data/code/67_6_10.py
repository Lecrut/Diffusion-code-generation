UNIT_CONVERSION_FACTOR = 1000

def validate_positive(value):
    if value < 0:
        raise ValueError("Volume must be non-negative")
    return value

def liters_to_milliliters(liters):
    return validate_positive(liters) * UNIT_CONVERSION_FACTOR

if __name__ == '__main__':
    input_liters = 250
    output_milliliters = liters_to_milliliters(input_liters)
    print(output_milliliters)