def convert_kilometers_to_meters(kilometer_values):
    return [km * 1000 for km in kilometer_values]

if __name__ == '__main__':
    km_values = [1, 5.5, 10, 0.2, 100]
    meter_values = convert_kilometers_to_meters(km_values)
    print(meter_values)