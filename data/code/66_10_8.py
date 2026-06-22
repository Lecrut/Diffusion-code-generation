def km_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [1, 0.5, 10, 0, 123.456]
    for val in test_values:
        print(km_to_meters(val))