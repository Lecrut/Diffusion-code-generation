def compute_sum_diff(x: int, y: int) -> (int, int):
    sum_result = x + y
    diff_result = x - y
    return sum_result, diff_result

if __name__ == '__main__':
    sample_a = 15
    sample_b = 7
    output = compute_sum_diff(sample_a, sample_b)
    print(output)