import numpy as np

def divide_and_handle_zero(numerator, denominator):
    return np.where(denominator != 0, numerator / denominator, 0)

if __name__ == '__main__':
    sample_numerator = np.array([10, 20, 30, 40])
    sample_denominator = np.array([2, 0, 5, 0])
    result = divide_and_handle_zero(sample_numerator, sample_denominator)
    print(result)