def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    result = evaluate_expression(sample_a, sample_b, sample_c)
    print(result)