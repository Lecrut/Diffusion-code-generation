CONVERSION_FACTOR = 1000

def convert_kilometers_to_meters(kilometers):
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 5
    meter_value = convert_kilometers_to_meters(sample_kilometers)
    print(meter_value)