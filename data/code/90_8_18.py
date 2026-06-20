def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    a_sample = 6
    b_sample = 9
    result = evaluate_or_condition(a_sample, b_sample)
    print(f"Result for (a > 5) or (b < 10): {result}")