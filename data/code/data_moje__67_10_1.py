def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    sample_liters = 2.5
    result = liters_to_milliliters(sample_liters)
    print(result)
    sample_liters = 0.1
    result = liters_to_milliliters(sample_liters)
    print(result)
    sample_liters = 100.0
    result = liters_to_milliliters(sample_liters)
    print(result)