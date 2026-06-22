def convert_to_milliliters(liters):
    return liters * 1000

if __name__ == "__main__":
    test_cases = [1.0, 2.5, 0.001, 50, 100.75]
    results = list(map(convert_to_milliliters, test_cases))
    print(results)