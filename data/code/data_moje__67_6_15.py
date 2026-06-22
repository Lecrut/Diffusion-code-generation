CONVERSION_FACTOR = 1000

def liters_to_milliliters(liters: int) -> int:
    return liters * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 42
    print(liters_to_milliliters(sample_value))