def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [0.5, 1, 2.5, 10, 100]
    print(f"{'Kilometers':<12} {'Meters':<10}")
    print("-" * 22)
    for km in test_cases:
        meters = convert_kilometers_to_meters(km)
        print(f"{km:<12.1f} {meters:<10.0f}")