import numpy as np

def check_zero_values(numbers):
    numbers_array = np.array(numbers, dtype=complex)
    tolerance = 1e-10
    zero_mask = np.isclose(numbers_array, 0 + 0j, atol=tolerance)
    return zero_mask
if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-15, -1e-15, 1 + 0j, -1 + 0j, 1e-16 + 1e-16j, 0j]
    zero_mask = check_zero_values(sample_values)
    print(zero_mask)