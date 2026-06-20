def evaluate_and_condition(a, b):
    return a and b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = evaluate_and_condition(sample_a, sample_b)
    print(result)