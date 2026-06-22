CONVERSION_FACTOR = 1000
km_to_m = lambda value: value * CONVERSION_FACTOR

if __name__ == '__main__':
    input_kilometers = 5
    output_meters = km_to_m(input_kilometers)
    print(output_meters)