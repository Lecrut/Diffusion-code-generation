def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    test_values = [1.0, 0.5, 2.75, 0.001]
    for value in test_values:
        result = liters_to_milliliters(value)
        print(result)