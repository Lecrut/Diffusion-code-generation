import numpy as np

def check_zero_values(numbers):
    numbers_array = np.array(numbers, dtype=complex)
    tolerance = 1e-10
    zero_mask = np.isclose(numbers_array, 0 + 0j, atol=tolerance)
    return zero_mask
if __name__ == '__main__':
    sample_values = [0, 1e-15, -1e-15, 3.14, 2 + 0j, 0j, 1 + 1j, -1 - 1j]
    result = check_zero_values(sample_values)
    print(result)