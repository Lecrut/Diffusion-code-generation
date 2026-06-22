def milliliters_to_liters(ml):
    if ml < 0:
        raise ValueError("Negative values are not allowed")
    return ml / 1000

if __name__ == '__main__':
    sample_value = 500
    result = milliliters_to_liters(sample_value)
    print(result)