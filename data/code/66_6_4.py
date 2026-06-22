def meter_generator():
    kilometers = [1, 2, 5, 10, 100]
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    for meters in meter_generator():
        print(meters)