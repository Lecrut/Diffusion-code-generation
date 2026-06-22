CONVERSION_FACTOR = 1000

def convert_liters_to_milliliters(volume_in_liters: int) -> int:
    return volume_in_liters * CONVERSION_FACTOR

if __name__ == "__main__":
    sample_value = 10
    converted = convert_liters_to_milliliters(sample_value)
    print(converted)