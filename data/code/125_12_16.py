def compute_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    sum_result, diff_result = compute_operations(sample_a, sample_b)
    print(f"Sum: {sum_result}, Difference: {diff_result}")