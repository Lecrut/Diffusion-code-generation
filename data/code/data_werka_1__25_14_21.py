import numpy as np

def is_effectively_zero(values):
    zero_mask = np.zeros(len(values), dtype=bool)
    for i, value in enumerate(values):
        if isinstance(value, int):
            zero_mask[i] = (value == 0)
        elif isinstance(value, float):
            zero_mask[i] = np.isclose(value, 0.0)
        elif isinstance(value, complex):
            zero_mask[i] = np.isclose(value.real, 0.0) and np.isclose(value.imag, 0.0)
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-10, -1e-10, 1+0j, 0+1j, 0+0j, 1+1j]
    result = is_effectively_zero(sample_values)
    print(result)