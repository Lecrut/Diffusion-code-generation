def km_to_meters_generator():
    distances_km = [1.0, 5.5, 10, 100.5, 0.1]
    for km in distances_km:
        yield km * 1000

if __name__ == '__main__':
    for value in km_to_meters_generator():
        print(value)