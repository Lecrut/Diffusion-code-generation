def liters_to_milliliters(liters):
    if liters is None:
        return None
    if not isinstance(liters, (int, float)):
        return None
    if liters < 0:
        return None
    if liters == 0:
        return 0
    return liters * 1000

if __name__ == '__main__':
    samples = [5, 0, -1, None, 0.5, "abc"]
    for sample in samples:
        result = liters_to_milliliters(sample)
        print(result)