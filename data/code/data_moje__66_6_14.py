def meter_generator():
    kilometers = [1.5, 2.3, 4.0, 7.8, 10.0]
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    for meter_value in meter_generator():
        print(meter_value)