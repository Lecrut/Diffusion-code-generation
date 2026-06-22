def km_to_meters(km):
    return km * 1000

def convert_km_to_meters(km_tuple):
    return tuple(map(km_to_meters, km_tuple))

if __name__ == '__main__':
    kilometers = (1.5, 2.0, 3.75, 10.0)
    meters = convert_km_to_meters(kilometers)
    print(meters)