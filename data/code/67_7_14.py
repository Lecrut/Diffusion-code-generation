def liters_to_milliliters(liters: float) -> float:
    if not isinstance(liters, (int, float)):
        raise TypeError("Input must be a numeric type")
    if isinstance(liters, bool):
        raise TypeError("Input must be a numeric type")
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(2.5))
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(10))