import numpy as np

def is_zero_within_tolerance(value, tolerance=1e-10):
    if isinstance(value, (int, float)):
        return np.isclose(value, 0, atol=tolerance)
    elif isinstance(value, complex):
        return np.isclose(value.real, 0, atol=tolerance) and np.isclose(value.imag, 0, atol=tolerance)
    else:
        raise ValueError(f"Unsupported type: {type(value)}")

def check_zero_values(values):
    zero_mask = [is_zero_within_tolerance(value) for value in values]
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 1e-9, -1e-9, 0.0, 1+0j, 0+0j, 1e-14 + 1e-14j, 2.71828, -3.14159]
    result = check_zero_values(sample_values)
    print(result)