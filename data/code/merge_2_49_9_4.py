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
    sample_data_1 = [1.5, 3.2, -4.8]
    sample_data_2 = [5.0, 5.0, 5.0]
    result_1 = is_positive_result(sample_data_1)
    result_2 = is_positive_result(sample_data_2)
    print(f"Dataset 1 Positive Result: {result_1}")
    print(f"Dataset 2 Positive Result: {result_2}")