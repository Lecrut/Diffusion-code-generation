def liters_to_milliliters(liters):
    if liters < 0:
        return None
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(-1))
    print(liters_to_milliliters(1))
    print(liters_to_milliliters(2.5))
    print(liters_to_milliliters(1000))