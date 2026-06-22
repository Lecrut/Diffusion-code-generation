KILOMETER_TO_METER_FACTOR = 1000

def convert_kilometers_to_meters(kilometers):
    return kilometers * KILOMETER_TO_METER_FACTOR

if __name__ == '__main__':
    sample_kilometers = 42
    meters = convert_kilometers_to_meters(sample_kilometers)
    print(meters)