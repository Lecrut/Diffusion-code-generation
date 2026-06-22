def km_to_meters(kilometers):
    return kilometers * 1000

def main():
    test_cases = [1.0, 2.5, 10.0, 0.0, 100.0]
    print(f"{'Kilometers':<12} | {'Meters':<12}")
    print("-" * 27)
    for km in test_cases:
        meters = km_to_meters(km)
        print(f"{km:<12} | {meters:<12}")

if __name__ == '__main__':
    main()