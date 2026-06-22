def liters_to_milliliters(liters: float) -> float:
    if not isinstance(liters, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(1.5))
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(2))
    try:
        liters_to_milliliters("not a number")
    except TypeError as e:
        print(e)