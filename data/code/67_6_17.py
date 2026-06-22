CONVERT_FACTOR = 1000

def liters_to_milliliters(liters):
    if liters is None:
        return None
    if not isinstance(liters, (int, float)):
        raise TypeError("Expected numeric input")
    return liters * CONVERT_FACTOR

if __name__ == '__main__':
    sample = 3
    print(liters_to_milliliters(sample))