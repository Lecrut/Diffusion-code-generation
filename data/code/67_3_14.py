import numpy as np

def convert_liters_to_milliliters(liters_array):
    liters_array = np.asarray(liters_array, dtype=np.float64)
    return liters_array * 1000.0

if __name__ == '__main__':
    sample_values = np.array([1.0, 2.5, 0.001, 50.0, 1000.0])
    result = convert_liters_to_milliliters(sample_values)
    print(result)