def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

if __name__ == '__main__':
    test_cases = [0.0, 1.0, 0.5, 2.25, 100.0, 0.001, -0.5]
    for liters in test_cases:
        result = liters_to_milliliters(liters)
        print(result)