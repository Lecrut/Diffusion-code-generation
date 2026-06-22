import numpy as np

def is_effectively_zero(values):
    def is_zero(x):
        if isinstance(x, int):
            return x == 0
        elif isinstance(x, float):
            return np.isclose(x, 0.0)
        elif isinstance(x, complex):
            return np.isclose(x.real, 0.0) and np.isclose(x.imag, 0.0)
        else:
            raise ValueError(f"Unsupported type: {type(x)}")
    
    return [is_zero(v) for v in values]

if __name__ == '__main__':
    sample_values = [0, 1e-10, -1e-10, 0j, 1+0j, 0+1j, 1.0, -1.0, 0.0]
    result = is_effectively_zero(sample_values)
    print(result)