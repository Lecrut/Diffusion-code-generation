def evaluate_expression(a, b, c):
    condition1 = a > b
    condition2 = not (c < 0)
    result = condition1 and condition2
    return result

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    sample_c = 4
    if evaluate_expression(sample_a, sample_b, sample_c):
        print(f"Expression is True: ({sample_a} > {sample_b}) AND not ({sample_c} < 0)")
    else:
        print(f"Expression is False: ({sample_a} > {sample_b}) AND not ({sample_c} < 0)")