import numpy as np

def check_zero_values(values):
    values_array = np.array(values, dtype=complex)
    tolerance = 1e-10
    zero_mask = np.isclose(values_array.real, 0.0, atol=tolerance) & np.isclose(values_array.imag, 0.0, atol=tolerance)
    return zero_mask
if __name__ == '__main__':
    sample_values = [0, 1e-15, -1e-15, 1 + 1j, 1 - 1j, 0j, 1e-16 + 1e-16j]
    result = check_zero_values(sample_values)
    print(result)