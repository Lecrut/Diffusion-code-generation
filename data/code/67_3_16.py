import numpy as np

def convert_liters_to_milliliters(liters):
    liters_array = np.asarray(liters, dtype=np.float64)
    return liters_array * 1000.0

if __name__ == '__main__':
    sample_values = np.array([0.0, 1.0, 2.5, 10.0, 0.001])
    result = convert_liters_to_milliliters(sample_values)
    print(result)