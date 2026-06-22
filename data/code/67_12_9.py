def liters_to_milliliters(liters):
    if liters < 0:
        return None
    if liters == 0:
        return 0.0
    return liters * 1000.0

if __name__ == '__main__':
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(-5))
    print(liters_to_milliliters(1.5))
    print(liters_to_milliliters(100))