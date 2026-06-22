def convert_liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    sample_liters = [0.5, 1, 2.5, 10]
    results = map(convert_liters_to_milliliters, sample_liters)
    for result in results:
        print(result)