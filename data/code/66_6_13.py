def kilometer_to_meter(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_km = [1.5, 2.0, 3.75, 10.0]
    meter_values = list(kilometer_to_meter(sample_km))
    print(meter_values)