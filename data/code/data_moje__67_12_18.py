def liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        return None
    if liters < 0:
        return None
    if liters == 0:
        return 0.0
    return liters * 1000.0

if __name__ == '__main__':
    test_values = [5, 0, -3, 2.5, "abc"]
    for value in test_values:
        result = liters_to_milliliters(value)
        print(result)