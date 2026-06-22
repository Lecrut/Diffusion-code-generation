UNIT_CONVERSION_FACTOR = 1000

def liters_to_milliliters(volume):
    if not isinstance(volume, (int, float)):
        return None
    if volume < 0:
        return None
    return volume * UNIT_CONVERSION_FACTOR

if __name__ == '__main__':
    inputs = [2.5, 0, -10, 0.75, "text"]
    for v in inputs:
        print(liters_to_milliliters(v))