def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

if __name__ == '__main__':
    test_cases = [0.0, 1.5, 3.75, -2.0, 100.123456]
    for value in test_cases:
        print(liters_to_milliliters(value))