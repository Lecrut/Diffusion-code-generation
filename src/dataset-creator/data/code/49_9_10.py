import math
def is_positive_result(values):
    n = len(values)
    if n < 2:
        return False
    total_sum = sum(values)
    mean = total_sum / n
    variance = sum((x - mean) ** 2 for x in values)
    return variance > 1e-9
if __name__ == '__main__':
    sample_data = [2.5, 3.7, -4.1, 0.0]
    result_flag = is_positive_result(sample_data)
    if result_flag:
        print("Result is positive.")
    else:
        print("Result is not strictly positive (zero or negative).")