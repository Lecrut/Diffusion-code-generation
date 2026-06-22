import numpy as np

def is_effectively_zero(values, tolerance=1e-10):
    mask = np.zeros(len(values), dtype=bool)
    for i, value in enumerate(values):
        if isinstance(value, int):
            mask[i] = (value == 0)
        elif isinstance(value, float):
            mask[i] = abs(value) < tolerance
        elif isinstance(value, complex):
            mask[i] = abs(value.real) < tolerance and abs(value.imag) < tolerance
    return mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-15, -1e-12, 1+0j, 0+0j, 1e-9 + 1e-10j, -1e-11 - 1e-10j]
    result = is_effectively_zero(sample_values)
    print(result)