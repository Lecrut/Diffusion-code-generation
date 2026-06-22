import numpy as np

def liters_to_milliliters(liters_array):
    liters_np = np.asarray(liters_array, dtype=np.float64)
    return liters_np * 1000.0

if __name__ == '__main__':
    sample_liters = [1.5, 0.25, 2.0, 0.001]
    result = liters_to_milliliters(sample_liters)
    print(result)