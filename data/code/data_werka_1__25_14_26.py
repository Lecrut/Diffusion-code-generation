import numpy as np

def is_effectively_zero(values):
    mask = []
    for value in values:
        if isinstance(value, complex):
            mask.append(np.isclose(value.real, 0) and np.isclose(value.imag, 0))
        elif isinstance(value, (int, float)):
            mask.append(np.isclose(value, 0))
        else:
            mask.append(False)
    return mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-10, -1e-10, 1+0j, 0+1j, 0+0j, 1.0+1e-10j, 2+3j]
    zero_mask = is_effectively_zero(sample_values)
    print(zero_mask)