def convert_km_to_m(km):
    return km * 1000

if __name__ == '__main__':
    test_values = [1, 2.5, 100, 0]
    for km in test_values:
        result = convert_km_to_m(km)
        print(result)