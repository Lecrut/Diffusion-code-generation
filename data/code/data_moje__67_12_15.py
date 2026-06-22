def _validate_input(value):
    if not isinstance(value, (int, float)):
        return False
    if isinstance(value, bool):
        return False
    if value < 0:
        return False
    return True

LITERS_TO_MILLILITERS_FACTOR = 1000

def liters_to_milliliters(liters):
    if not _validate_input(liters):
        return None
    if liters == 0:
        return 0
    return liters * LITERS_TO_MILLILITERS_FACTOR

if __name__ == '__main__':
    test_cases = [2.5, 0, -10, 100, "text", True, 0.0]
    for case in test_cases:
        print(liters_to_milliliters(case))