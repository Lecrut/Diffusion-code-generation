def evaluate_conditions(a: int, b: int, c: int) -> bool:
    POSITIVE_THRESHOLD = 0
    MINIMUM_POSITIVE_COUNT = 2
    conditions = [val > POSITIVE_THRESHOLD for val in (a, b, c)]
    return conditions.count(True) >= MINIMUM_POSITIVE_COUNT

if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)