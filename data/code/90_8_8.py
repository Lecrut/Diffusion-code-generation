def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    sample_a = 6
    sample_b = 9
    result = evaluate_or_condition(sample_a, sample_b)
    print(result)