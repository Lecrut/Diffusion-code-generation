import numpy as np

def is_effectively_zero(values, tolerance=1e-10):
    mask = np.zeros(len(values), dtype=bool)
    for i, value in enumerate(values):
        if isinstance(value, int) or (isinstance(value, float) and abs(value) < tolerance):
            mask[i] = True
        elif isinstance(value, complex) and (abs(value.real) < tolerance and abs(value.imag) < tolerance):
            mask[i] = True
    return mask

if __name__ == '__main__':
    sample_values = [0, 1e-15, 1.0, 2+0j, 3-1e-10j, 4.00000000001, 5j]
    zero_mask = is_effectively_zero(sample_values)
    print(zero_mask)