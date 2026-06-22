def liters_to_milliliters(liters: float) -> float:
    if not isinstance(liters, (int, float)):
        raise TypeError("Expected a numeric type for liters")
    return liters * 1000

if __name__ == '__main__':
    sample_liters = 2.5
    result = liters_to_milliliters(sample_liters)
    print(result)