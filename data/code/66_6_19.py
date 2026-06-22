def kilometer_to_meter_generator():
    kilometer_values = [1, 2.5, 10, 0.1, 100]
    for km in kilometer_values:
        yield km * 1000

if __name__ == '__main__':
    generator = kilometer_to_meter_generator()
    meter_values = list(generator)
    print(meter_values)