def liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1, 2.5, 0.5, 10, 0.125]
    results = map(liters_to_milliliters, test_cases)
    print(list(results))