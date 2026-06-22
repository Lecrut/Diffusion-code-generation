KILOMETER_TO_METER_FACTOR = 1000.0

def convert_kilometers_to_meters(kilometers):
    return kilometers * KILOMETER_TO_METER_FACTOR

if __name__ == '__main__':
    kilometers = 5
    meters = convert_kilometers_to_meters(kilometers)
    print(meters)