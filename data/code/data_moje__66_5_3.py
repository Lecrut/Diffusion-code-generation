def kilometers_to_meters(kilometers):
    return kilometers * 1000

def main():
    test_cases = [1, 5, 10, 0, -3.5, 100.123]
    print("{:<15} {:<15}".format("Kilometers", "Meters"))
    print("-" * 30)
    for km in test_cases:
        meters = kilometers_to_meters(km)
        print("{:<15} {:<15}".format(km, meters))

if __name__ == '__main__':
    main()