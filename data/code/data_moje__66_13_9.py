CONVERSION_FACTOR = 1000

km_to_m = lambda x: x * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_km = 5
    meters = km_to_m(sample_km)
    print(meters)