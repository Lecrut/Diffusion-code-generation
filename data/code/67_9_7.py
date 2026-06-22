def convert_liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1, 2.5, 5, 10.75, 0.1]
    conversions = list(map(convert_liters_to_milliliters, test_cases))
    for original, converted in zip(test_cases, conversions):
        print(f"{original} liters is {converted} milliliters")