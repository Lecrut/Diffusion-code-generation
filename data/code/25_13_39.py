import numpy as np

def check_zero_values(numbers):
    numbers = np.array(numbers)
    zero_mask = np.isclose(numbers, 0, atol=1e-10)
    return zero_mask

if __name__ == '__main__':
    sample_values = [0, 0.0, 1e-15, -1e-15, 1+0j, 0+0j, 1e-20+1e-20j]
    result = check_zero_values(sample_values)
    print(result)