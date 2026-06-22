import numpy as np

def is_effectively_zero(values):
    zero_mask = []
    for value in values:
        if isinstance(value, complex):
            zero_mask.append(np.isclose(value.real, 0) and np.isclose(value.imag, 0))
        elif isinstance(value, (int, float)):
            zero_mask.append(np.isclose(value, 0))
        else:
            zero_mask.append(False)
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-10, -1e-10, 1+1j, 1-1j, 0j, 1e-20+1e-20j]
    result = is_effectively_zero(sample_values)
    print(result)