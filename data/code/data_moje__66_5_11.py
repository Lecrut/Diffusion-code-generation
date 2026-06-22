def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [1, 5, 10, 25, 100]
    print(f"{'Kilometers':<12} {'Meters':<12}")
    print("-" * 24)
    for km in test_cases:
        meters = convert_kilometers_to_meters(km)
        print(f"{km:<12} {meters:<12}")