def km_to_meters(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_km = [1, 2.5, 10, 0.1]
    meter_values = list(km_to_meters(sample_km))
    print(meter_values)