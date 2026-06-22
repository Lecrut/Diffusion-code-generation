import numpy as np

def liters_to_milliliters(liters_array):
    liters_array = np.asarray(liters_array, dtype=np.float64)
    return liters_array * 1000.0

if __name__ == '__main__':
    sample_liters = np.array([1.0, 0.5, 2.25, 0.001, 100.0])
    result = liters_to_milliliters(sample_liters)
    print(result)