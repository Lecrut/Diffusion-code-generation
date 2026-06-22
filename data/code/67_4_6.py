def liters_to_milliliters(liters):
    return liters * 1000

if __name__ == '__main__':
    test_cases = [1.0, 0.5, 2.5, 0.001, 10.0]
    for case in test_cases:
        print(liters_to_milliliters(case))