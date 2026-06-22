def convert_liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1.0, 2.5, 0.5, 10.0, 3.75]
    results = list(map(convert_liters_to_milliliters, test_cases))
    for result in results:
        print(result)