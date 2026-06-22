KILOMETER_TO_METER = 1000

def convert_km_to_m(km_value):
    return km_value * KILOMETER_TO_METER

if __name__ == '__main__':
    sample_km = 5
    meters = convert_km_to_m(sample_km)
    print(meters)