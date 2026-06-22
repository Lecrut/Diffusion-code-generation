def liters_to_milliliters(liters: float) -> float:
    if not isinstance(liters, (int, float)):
        raise TypeError("Input must be a numeric type")
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(2.5))
    print(liters_to_milliliters(1))
    try:
        print(liters_to_milliliters("invalid"))
    except TypeError as e:
        print(e)