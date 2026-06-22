def liters_to_milliliters(liters):
    return liters * 1000.0

if __name__ == '__main__':
    test_cases = [1.0, 0.5, 2.25, 0.001, 100.0]
    for value in test_cases:
        print(liters_to_milliliters(value))