def liters_to_milliliters(liters):
    if liters < 0:
        return None
    if liters == 0:
        return 0
    return liters * 1000

if __name__ == '__main__':
    test_values = [-5, 0, 1, 2.5]
    for val in test_values:
        print(liters_to_milliliters(val))