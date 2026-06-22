import numpy as np

def check_zero_values(values):
    zero_mask = []
    for value in values:
        if isinstance(value, int):
            zero_mask.append(value == 0)
        elif isinstance(value, float):
            zero_mask.append(np.isclose(value, 0.0))
        elif isinstance(value, complex):
            zero_mask.append(np.isclose(value.real, 0.0) and np.isclose(value.imag, 0.0))
        else:
            raise ValueError(f"Unsupported type: {type(value)}")
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-10, -1e-10, 1+0j, 0+0j, 1e-20+1e-20j]
    result = check_zero_values(sample_values)
    print(result)