def liters_to_milliliters(liters):
    if liters < 0:
        return None
    if liters == 0:
        return 0.0
    return liters * 1000

if __name__ == '__main__':
    sample_values = [1, 0.5, 0, -1, -0.1]
    for value in sample_values:
        result = liters_to_milliliters(value)
        print(result)