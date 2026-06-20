def evaluate_or_condition(a, b):
    return a > 10 or b > 10

if __name__ == '__main__':
    sample_a = 5
    sample_b = 12
    result = evaluate_or_condition(sample_a, sample_b)
    print(result)