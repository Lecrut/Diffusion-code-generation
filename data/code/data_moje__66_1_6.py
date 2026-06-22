KM_TO_METER_FACTOR = 1000

def km_to_meters(kilometers):
    return kilometers * KM_TO_METER_FACTOR

if __name__ == '__main__':
    sample_km = 5.0
    result = km_to_meters(sample_km)
    print(result)