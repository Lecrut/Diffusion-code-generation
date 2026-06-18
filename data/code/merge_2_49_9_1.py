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
    sample_data = [3, 5, 7, 2, 4]
    result = is_positive_result(sample_data)
    print(result)