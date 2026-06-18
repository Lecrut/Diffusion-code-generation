import math
def is_positive_result(values):
    total = 0
    n = len(values)
    current_sum = sum(values)
    if n <= 1:
        return False
    mean_val = current_sum / n
    for val in values:
        diff_sq = (val - mean_val) ** 2
        total += diff_sq
    return total > 0
if __name__ == '__main__':
    sample_data_1 = [1, 2, 3]
    sample_data_2 = [-5, -4, -3]
    result_a = is_positive_result(sample_data_1)
    result_b = is_positive_result(sample_data_2)
    print(f"Dataset A Positive: {result_a}")
    print(f"Dataset B Positive: {result_b}")