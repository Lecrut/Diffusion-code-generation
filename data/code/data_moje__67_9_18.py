def convert_liters_to_milliliters(liters_list):
    return list(map(lambda x: x * 1000, liters_list))

if __name__ == '__main__':
    test_cases = [1, 2.5, 10, 0.5]
    results = convert_liters_to_milliliters(test_cases)
    for original, converted in zip(test_cases, results):
        print(f"{original} liters is {converted} milliliters")