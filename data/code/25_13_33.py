import numpy as np

def is_effectively_zero(values):
    mask = []
    for value in values:
        if isinstance(value, int) or isinstance(value, float):
            mask.append(np.isclose(value, 0))
        elif isinstance(value, complex):
            mask.append(np.isclose(value.real, 0) and np.isclose(value.imag, 0))
        else:
            raise ValueError(f"Unsupported type: {type(value)}")
    return mask

if __name__ == '__main__':
    sample_values = [0, 1e-10, -1e-10, 0.0, 1+0j, 0+0j, 1e-15 + 1e-15j]
    result = is_effectively_zero(sample_values)
    print(result)