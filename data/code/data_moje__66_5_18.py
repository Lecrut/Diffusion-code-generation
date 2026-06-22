def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [
        (0, "0 km"),
        (1, "1 km"),
        (2.5, "2.5 km"),
        (10, "10 km"),
        (100, "100 km")
    ]

    print(f"{'Kilometers':<15} {'Meters':<15}")
    print("-" * 30)

    for km, label in test_cases:
        meters = convert_kilometers_to_meters(km)
        print(f"{label:<15} {meters:<15}")