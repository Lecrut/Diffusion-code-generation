def convert_liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    sample_liters = 1.5
    result = convert_liters_to_milliliters(sample_liters)
    print(result)