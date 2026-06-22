def convert_to_milliliters(liters):
    return liters * 1000

def run_tests():
    test_cases = [1, 2.5, 0, 10, -5]
    results = list(map(convert_to_milliliters, test_cases))
    for original, converted in zip(test_cases, results):
        print(f"{original} L = {converted} mL")

if __name__ == '__main__':
    run_tests()