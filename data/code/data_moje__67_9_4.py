def convert_liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1, 2.5, 3, 4.75, 5.0]
    results = list(map(convert_liters_to_milliliters, test_cases))
    print(results)