def km_to_m(kilometers):
    return kilometers * 1000

def main():
    test_cases = [0, 1, 5.5, 100, 1234.567]
    print(f"{'Kilometers':<15} | {'Meters':<15}")
    print("-" * 33)
    for km in test_cases:
        meters = km_to_m(km)
        print(f"{km:<15.3f} | {meters:<15.3f}")

if __name__ == '__main__':
    main()