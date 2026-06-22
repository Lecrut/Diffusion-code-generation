def liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [0.5, 1.0, 2.5, 7.33, 10.0]
    results = list(map(liters_to_milliliters, test_cases))
    print(results)