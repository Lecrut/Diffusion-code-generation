KILOMETER_TO_METER_FACTOR = 1000

def calculate_meter(kilometer_value):
    return kilometer_value * KILOMETER_TO_METER_FACTOR

def convert_kilometer_tuple_to_meter_tuple(kilometer_sequence):
    return tuple(map(calculate_meter, kilometer_sequence))

if __name__ == '__main__':
    test_kilometers = (15, 20.5, 0.25, 400, 1.75)
    meter_result = convert_kilometer_tuple_to_meter_tuple(test_kilometers)
    print(meter_result)