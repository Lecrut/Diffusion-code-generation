def evaluate_or_condition(a: int, b: int) -> bool:
    return a > 10 or b > 10

if __name__ == '__main__':
    sample_a = 7
    sample_b = 12
    result = evaluate_or_condition(sample_a, sample_b)
    print(result)