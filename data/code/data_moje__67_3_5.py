import numpy as np

def liters_to_milliliters(liters_array):
    return np.array(liters_array, dtype=np.float64) * 1000.0

if __name__ == '__main__':
    sample_litters = np.array([1.0, 0.5, 2.5, 0.001, 10.0])
    result = liters_to_milliliters(sample_litters)
    print(result)