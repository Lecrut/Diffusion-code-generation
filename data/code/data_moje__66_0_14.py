KILOMETER_TO_METER_FACTOR = 1000

def kilometers_to_meters(kilometers):
    return kilometers * KILOMETER_TO_METER_FACTOR

if __name__ == '__main__':
    sample_km = 10
    print(kilometers_to_meters(sample_km))