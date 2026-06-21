def evaluate_conditions(a: int, b: int, c: int) -> bool:
    POSITIVE_THRESHOLD = 0
    MINIMUM_POSITIVE_COUNT = 2
    positive_count = (a > POSITIVE_THRESHOLD) + (b > POSITIVE_THRESHOLD) + (c > POSITIVE_THRESHOLD)
    return positive_count >= MINIMUM_POSITIVE_COUNT

if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)