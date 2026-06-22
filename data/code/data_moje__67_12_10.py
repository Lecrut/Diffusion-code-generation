def liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        return None
    if liters <= 0:
        return None
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(5))
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(-2))
    print(liters_to_milliliters(1.5))