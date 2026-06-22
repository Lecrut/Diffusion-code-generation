def liters_to_milliliters(liters):
    milliliters = liters * 1000.0
    return milliliters
if __name__ == '__main__':
    test_cases = [1.0, 0.5, 2.25, 0.0, -1.0, 123.456789]
    for liters in test_cases:
        result = liters_to_milliliters(liters)
        print(result)