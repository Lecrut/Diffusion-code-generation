METERS_TO_KILOMETERS = 1 / 1000

def convert_meters_to_kilometers(meters):
    return meters * METERS_TO_KILOMETERS

if __name__ == '__main__':
    sample_value = 5000.0
    result = convert_meters_to_kilometers(sample_value)
    print(result)