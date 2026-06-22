def kilometer_to_meter_generator():
    kilometer_values = [1, 2.5, 10, 100, 0.5]
    for km in kilometer_values:
        yield km * 1000

if __name__ == '__main__':
    for meter in kilometer_to_meter_generator():
        print(meter)