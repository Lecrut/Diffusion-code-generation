import numpy as np

def check_zero_values(data):
    array = np.array(data, dtype=complex)
    tolerance = 1e-10
    zero_mask = np.isclose(array, 0, atol=tolerance)
    return zero_mask
if __name__ == '__main__':
    sample_data = [0, 0.0, 1e-15, -1e-15, 1 + 0j, 0 + 1j, 0 - 1j, 1e-16 + 1e-16j]
    zero_mask = check_zero_values(sample_data)
    print(zero_mask)