def kilometer_to_meter_generator(kilometers_list):
    for km in kilometers_list:
        yield km * 1000

if __name__ == '__main__':
    sample_kilometers = [1, 2.5, 10, 0.75]
    meter_values = kilometer_to_meter_generator(sample_kilometers)
    for value in meter_values:
        print(value)