def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) and (c == 5) and (d is not None)
    return result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    sample_c = 5
    sample_d = "value"
    output = evaluate_conditions(sample_a, sample_b, sample_c, sample_d)
    print(output)