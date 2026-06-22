UNIT_CONVERSIONS = {
    'liters': 1000,
    'milliliters': 1
}

def liters_to_milliliters(liters: float) -> float:
    factor = UNIT_CONVERSIONS['liters']
    return liters * factor

if __name__ == '__main__':
    test_cases = [1.0, 0.5, 2.5, 100.0]
    for val in test_cases:
        ml = liters_to_milliliters(val)
        print(ml)