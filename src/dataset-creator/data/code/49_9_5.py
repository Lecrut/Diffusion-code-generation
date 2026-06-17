import math
def is_positive_result(values):
    n = len(values)
    if n < 2:
        return False
    total_sum = sum(values)
    mean = total_sum / n
    variance_sum = sum((x - mean) ** 2 for x in values)
    return variance_sum > 0
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = is_positive_result(sample_data)
    if result:
        print("Result is positive.")
    else:
        print("Result is not positive or zero.")