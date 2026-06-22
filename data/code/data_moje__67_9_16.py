def convert_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1, 2, 5, 10, 0.5]
    results = list(map(convert_to_milliliters, test_cases))
    print(results)