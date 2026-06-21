def evaluate_conditions(a: int, b: int, c: int) -> bool:
    thresholds = [a, b, c]
    positive_count = sum(1 for val in thresholds if val > 0)
    return positive_count >= 2

if __name__ == '__main__':
    sample_a = 10
    sample_b = -5
    sample_c = 0
    result = evaluate_conditions(sample_a, sample_b, sample_c)
    print(result)