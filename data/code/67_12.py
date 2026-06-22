def liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        return None
    if liters < 0:
        return None
    if liters == 0:
        return 0
    return liters * 1000

if __name__ == '__main__':
    test_values = [1.5, 0, -5, 0.001, "abc"]
    for val in test_values:
        result = liters_to_milliliters(val)
        print(result)