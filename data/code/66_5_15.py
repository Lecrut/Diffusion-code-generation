def kilometers_to_meters(kilometers):
    return kilometers * 1000

def main():
    test_cases = [0, 1, 2.5, 100, 1500]
    print("{:<10} {:<10}".format("Kilometers", "Meters"))
    print("-" * 20)
    for km in test_cases:
        meters = kilometers_to_meters(km)
        print("{:<10} {:<10}".format(km, meters))

if __name__ == '__main__':
    main()