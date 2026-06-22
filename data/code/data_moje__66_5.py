def km_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [1, 2.5, 10, 0, 100.123]
    header = f"{'Kilometers':<15} | {'Meters':<15}"
    separator = "-" * len(header)
    print(header)
    print(separator)
    for km in test_cases:
        meters = km_to_meters(km)
        print(f"{km:<15} | {meters:<15}")