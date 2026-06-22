def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    test_cases = [1, 5, 10, 100, 0.5]
    
    header = f"{'Kilometers':<15} {'Meters':<15}"
    print(header)
    print("-" * len(header))
    
    for km in test_cases:
        m = kilometers_to_meters(km)
        print(f"{km:<15} {m:<15}")