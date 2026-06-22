def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

if __name__ == '__main__':
    test_values = [1.0, 0.5, 2.5, 0.001, 100.0]
    for val in test_values:
        result = liters_to_milliliters(val)
        print(result)