import numpy as np

def liters_to_milliliters(liters_array):
    liters = np.asarray(liters_array, dtype=np.float64)
    return liters * 1000.0

if __name__ == '__main__':
    sample_liters = np.array([1.0, 0.5, 2.5, 0.25, 10.0])
    result = liters_to_milliliters(sample_liters)
    print(result)