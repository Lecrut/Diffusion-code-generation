def liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        raise ValueError("Volume must be a number")
    return liters * 1000

if __name__ == '__main__':
    sample_liters = 4.75
    milliliters = liters_to_milliliters(sample_liters)
    print(milliliters)