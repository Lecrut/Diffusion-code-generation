CONVERSION_FACTOR = 3.28084

def meters_to_feet(meters):
    return meters * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 10
    result = meters_to_feet(sample_value)
    print(result)