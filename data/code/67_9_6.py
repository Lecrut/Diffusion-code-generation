def convert_to_milliliters(liter_values):
    return list(map(lambda liters: liters * 1000, liter_values))

if __name__ == '__main__':
    test_cases = [1, 2.5, 0.5, 10, 0.1]
    results = convert_to_milliliters(test_cases)
    print(results)