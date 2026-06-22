def convert_liters_to_milliliters(liters_list):
    return list(map(lambda l: l * 1000, liters_list))

if __name__ == '__main__':
    test_cases = [1, 2.5, 0.5, 10]
    results = convert_liters_to_milliliters(test_cases)
    print(results)