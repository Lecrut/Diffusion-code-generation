LITER_TO_MILLILITER_FACTOR = 1000

def liters_to_milliliters(liters: float) -> float:
    if liters < 0:
        raise ValueError("Liters cannot be negative")
    return liters * LITER_TO_MILLILITER_FACTOR

if __name__ == '__main__':
    test_cases = [5.25, 0.004, 100.0]
    for value in test_cases:
        print(liters_to_milliliters(value))