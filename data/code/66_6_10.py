def kilometer_to_meter_generator(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    hard_coded_kilometers = [1, 5, 10, 25, 100]
    meter_values = list(kilometer_to_meter_generator(hard_coded_kilometers))
    print(meter_values)