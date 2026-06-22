def kilometer_to_meter_generator(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_kilometers = [1, 2.5, 10, 0, 100]
    meter_values = kilometer_to_meter_generator(sample_kilometers)
    for meter in meter_values:
        print(meter)