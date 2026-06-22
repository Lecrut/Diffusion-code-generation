def convert_km_to_m(km):
    return km * 1000

if __name__ == '__main__':
    test_cases = [1, 5, 10, 100, 0.5]
    
    header = f"{'Kilometers':<15} {'Meters':<15}"
    separator = '-' * 30
    print(header)
    print(separator)
    
    for km in test_cases:
        meters = convert_km_to_m(km)
        print(f"{km:<15} {meters:<15}")