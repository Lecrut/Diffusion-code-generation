def convert_liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        return None
    if liters < 0:
        return None
    if liters == 0:
        return 0
    return liters * 1000

if __name__ == '__main__':
    sample_values = [5, 0, -3, 1.5]
    for val in sample_values:
        result = convert_liters_to_milliliters(val)
        print(result)