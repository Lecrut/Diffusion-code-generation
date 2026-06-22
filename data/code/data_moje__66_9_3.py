KILometers_TO_METERS_FACTOR = 1000

def apply_conversion(km_value):
    return km_value * KILometers_TO_METERS_FACTOR

def transform_kilometer_tuple(kilometer_input):
    return tuple(map(apply_conversion, kilometer_input))

if __name__ == '__main__':
    sample_kilometers = (3.2, 7.8, 15.0, 0.25, 99.99)
    converted_meters = transform_kilometer_tuple(sample_kilometers)
    print(converted_meters)