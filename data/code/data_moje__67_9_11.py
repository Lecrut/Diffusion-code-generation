def convert_to_milliliters(liters):
    return liters * 1000

if __name__ == "__main__":
    test_cases = [1.5, 2.0, 0.25, 10, 0.1]
    results = list(map(convert_to_milliliters, test_cases))
    print(results)