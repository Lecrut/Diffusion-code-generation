def km_to_m(kilometers):
    return int(kilometers * 1000 + 0.5)

if __name__ == '__main__':
    test_values = [1.0, 2.5, 0.001, 10.123456, 0.9999]
    for value in test_values:
        result = km_to_m(value)
        print(result)