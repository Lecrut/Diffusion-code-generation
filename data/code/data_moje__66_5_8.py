def convert_km_to_m(kilometers):
    return kilometers * 1000

def main():
    test_cases = [1, 5.5, 0, 100.25, 3.14]
    print(f"{'Kilometers':<15} | {'Meters':>10}")
    print("-" * 30)
    for km in test_cases:
        meters = convert_km_to_m(km)
        print(f"{km:<15} | {meters:>10}")

if __name__ == '__main__':
    main()