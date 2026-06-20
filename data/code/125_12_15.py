def compute_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    return sum_result, difference_result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    sum_result, difference_result = compute_operations(sample_a, sample_b)
    print(f"Sum: {sum_result}, Difference: {difference_result}")