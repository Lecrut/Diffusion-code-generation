import numpy as np

def is_effectively_zero(values):
    mask = []
    for value in values:
        if isinstance(value, complex):
            mask.append(np.isclose(value.real, 0) and np.isclose(value.imag, 0))
        elif isinstance(value, float):
            mask.append(np.isclose(value, 0.0))
        else:
            mask.append(value == 0)
    return mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-10, -1e-15, 1j, 0+0j, 2+3j, 0j]
    result = is_effectively_zero(sample_values)
    print(result)