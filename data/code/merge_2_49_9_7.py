import math
def is_positive_result(values):
    total = sum(values)
    return total > 0
if __name__ == '__main__':
    sample_data = [1, -2, 3, 4, -5] * 10_000_000
    result = is_positive_result(sample_data)
    print(result)