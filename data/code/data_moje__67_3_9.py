import numpy as np

def convert_liters_to_milliliters(liters_array):
    arr = np.asarray(liters_array, dtype=np.float64)
    return arr * 1000.0

if __name__ == '__main__':
    sample_liters = np.array([1.5, 0.0, 2.5, 10.0])
    result = convert_liters_to_milliliters(sample_liters)
    print(result)