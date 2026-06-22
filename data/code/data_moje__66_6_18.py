def km_to_meters_generator():
    kilometers = [1, 2, 3, 5, 10, 0.5, 100.25]
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    result = list(km_to_meters_generator())
    print(result)