import numpy as np

def is_effectively_zero(numbers):
    numbers_array = np.array(numbers, dtype=np.complex128)
    return np.isclose(numbers_array.real, 0.0, atol=1e-10) & np.isclose(numbers_array.imag, 0.0, atol=1e-10)
if __name__ == '__main__':
    sample_values = [0, 0.0, complex(0, 0), 1e-15, -1e-15, complex(1e-15, -1e-15)]
    result = is_effectively_zero(sample_values)
    print(result)