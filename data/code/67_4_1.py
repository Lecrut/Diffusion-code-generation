def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    print(liters_to_milliliters(1.5))
    print(liters_to_milliliters(0))
    print(liters_to_milliliters(0.001))
    print(liters_to_milliliters(100.0))
    print(liters_to_milliliters(-5.0))