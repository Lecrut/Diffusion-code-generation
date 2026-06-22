KM_TO_M_FACTOR = 1000
km_to_m = lambda kilometers: kilometers * KM_TO_M_FACTOR
if __name__ == '__main__':
    sample_kilometers = 25
    converted_meters = km_to_m(sample_kilometers)
    print(converted_meters)