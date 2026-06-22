def check_sum_vs_difference(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val > diff_val

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = check_sum_vs_difference(sample_a, sample_b)
    print(result)