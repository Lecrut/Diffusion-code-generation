import numpy as np

def convert_to_milliliters(liters_array):
    liters_array = np.asarray(liters_array, dtype=np.float64)
    return liters_array * 1000.0
if __name__ == '__main__':
    sample_liters = np.array([1.5, 2.0, 0.25])
    result = convert_to_milliliters(sample_liters)
    print(result)