def kilometers_to_meters(kilometers):
    return kilometers * 1000

def main():
    test_cases = [0, 1, 5.5, 100, 0.001]
    
    print(f"{'Kilometers':<12} | {'Meters':<12}")
    print("-" * 26)
    
    for km in test_cases:
        meters = kilometers_to_meters(km)
        print(f"{km:<12} | {meters:<12}")

if __name__ == '__main__':
    main()