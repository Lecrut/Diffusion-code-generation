def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [1, 2.5, 10, 0.75, 100]
    print(f"{'Kilometers':<15} {'Meters':<15}")
    print("-" * 30)
    for km in test_cases:
        meters = convert_kilometers_to_meters(km)
        print(f"{km:<15} {meters:<15}")