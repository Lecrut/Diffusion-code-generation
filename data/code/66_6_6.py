def km_to_meters_generator():
    kilometers = [1, 5, 10, 100, 1000]
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    for meter in km_to_meters_generator():
        print(meter)