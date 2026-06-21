import numpy as np

def check_zero_values(values):
    zero_mask = []
    for value in values:
        if isinstance(value, int) or isinstance(value, float):
            zero_mask.append(np.isclose(value, 0))
        elif isinstance(value, complex):
            zero_mask.append(np.isclose(value.real, 0) and np.isclose(value.imag, 0))
        else:
            raise ValueError("Unsupported type")
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 1.0e-10, 0j, 1+0j, 2+3j, -0.0, 0.0000000001]
    print(check_zero_values(sample_values))