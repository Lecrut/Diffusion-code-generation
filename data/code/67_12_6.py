def liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        return None
    if liters < 0:
        return None
    if liters == 0:
        return 0
    return liters * 1000

if __name__ == '__main__':
    result = liters_to_milliliters(2.5)
    print(result)
    result_zero = liters_to_milliliters(0)
    print(result_zero)
    result_negative = liters_to_milliliters(-1)
    print(result_negative)