def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_a, sample_b, sample_c, sample_d = True, False, True, False
    result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(result)