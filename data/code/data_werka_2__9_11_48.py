def liters_to_milliliters(liters):
    conversion_factor = 1000
    return liters * conversion_factor

if __name__ == '__main__':
    sample_liters = 2.3
    milliliters = liters_to_milliliters(sample_liters)
    print(milliliters)