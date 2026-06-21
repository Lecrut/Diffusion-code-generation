def evaluate_conditions(a: int, b: int, c: int) -> bool:
    MINIMUM_POSITIVE_COUNT = 2
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    return positive_count >= MINIMUM_POSITIVE_COUNT

if __name__ == '__main__':
    result = evaluate_conditions(10, -5, 20)
    print(result)