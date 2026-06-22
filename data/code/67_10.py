def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

if __name__ == '__main__':
    sample_liters = 2.5
    result = liters_to_milliliters(sample_liters)
    print(result)
    sample_liters_2 = 0.001
    result_2 = liters_to_milliliters(sample_liters_2)
    print(result_2)