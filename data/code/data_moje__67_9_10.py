def convert_to_milliliters(liters: float) -> float:
    return liters * 1000

test_cases = [1, 2.5, 0.5, 10, 0.1]

if __name__ == '__main__':
    results = list(map(convert_to_milliliters, test_cases))
    for original, converted in zip(test_cases, results):
        print(f"{original} L = {converted} mL")