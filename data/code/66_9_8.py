def km_to_meters(km):
    return km * 1000

def convert_km_to_meters(km_values):
    return list(map(km_to_meters, km_values))

if __name__ == '__main__':
    sample_km = (1.0, 2.5, 5.0, 10.0, 0.5)
    result = convert_km_to_meters(sample_km)
    print(result)